---
name: yyds-router
description: 把客户端 / 脚本接到 YYDS Router（一个 OpenAI / Anthropic / Gemini 三种协议原生的模型网关）。当用户要「换 base URL 接 Claude/GPT/Gemini」「配 Claude Code / Codex / Cherry Studio」「调 /v1/messages 或 Gemini generateContent」「生成图片」时用。
---

# 接 YYDS Router

一个域名、一把令牌、一套计费。三种请求形状都指向同一批模型：

| 形状 | 路径 | 认证头 |
| --- | --- | --- |
| OpenAI 兼容 | `POST /v1/chat/completions`、`GET /v1/models` | `Authorization: Bearer sk-...` |
| OpenAI Responses | `POST /v1/responses` | 同上 |
| Anthropic | `POST /v1/messages` | `x-api-key: sk-...` + `anthropic-version: 2023-06-01` |
| Gemini | `POST /v1beta/models/{model}:generateContent` | `x-goog-api-key: sk-...` |
| 图像 | `POST /v1/images/generations` | `Authorization: Bearer sk-...` |

Base：`https://yydsrouter.com`（**Anthropic 形状不要带 `/v1`**，客户端自己拼；其它形状带 `/v1`）。

## 步骤

1. **确认令牌能用**：`curl -s https://yydsrouter.com/v1/models -H "Authorization: Bearer $TOKEN"` 能列出模型（401 = 令牌不对）。
2. **按客户端挑形状**：
   - Claude Code：`~/.claude/settings.json` → `env.ANTHROPIC_BASE_URL=https://yydsrouter.com`、`ANTHROPIC_AUTH_TOKEN=sk-...`、`ANTHROPIC_MODEL=claude-haiku-5.5`。
   - Codex CLI：`~/.codex/config.toml` → `base_url="https://yydsrouter.com/v1"`、`env_key="YYDS_API_KEY"`、`wire_api="responses"`。
   - 其它 OpenAI 兼容客户端：只改 `base_url` 为 `https://yydsrouter.com/v1`。
3. **先跑一发最小请求**（`max_tokens: 64`，消息 `只回两个字：收到`），再谈业务逻辑。

## 必须知道的坑

- **思考型模型**（Gemini 全系、Claude 全系、GPT 6 系）先思考再作答，`max_tokens` 给小了会被思考吃光、正文为空但照扣钱 → **≥ 200**。
- **GPT 6 系用 `max_completion_tokens`**（`max_tokens` 官方 API 不收，网关会转，但直连官方会 400）。
- **`gpt-6-luna` 不把 `max_tokens` 当上限**：给了也可能跑完 ~1300 个思考 token，控成本用 `max_completion_tokens`。
- **GPT 6.2 系超过 27.2 万 token 整笔涨价**（输入翻倍、输出 1.5 倍），不是超出部分加价。
- **图像**：`n` 最多 4；不传 `quality` 按最低档计价；2.5 系只有约 1024，要 2K/4K 选 2.6 系。
- **失败不扣费**：参数错误 / 超输出上限 / 上游报错都记 `quota=0`。
- 错误体统一是 `{"error":{"message":"...","type":"yydsai_error"}}`。

## 不要做

- 不要把令牌写进前端代码或仓库。
- 不要按"官方 SDK 的默认 base"去猜路径——Anthropic 与 Gemini 形状的路径前缀不一样（见上表）。
- 不要承诺上游可用性：每个模型只挂一条渠道，故障时回 503。
