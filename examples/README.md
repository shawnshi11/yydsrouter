# 示例代码

全部示例都只依赖一个令牌（控制台「API 密钥」里创建），把 `TOKEN` 换成 `sk-...` 就能跑。
网关不做任何"私有 SDK"：它就是一个 OpenAI / Anthropic / Gemini 兼容的 HTTP 端点，用官方 SDK 直连即可。

| 文件 | 说什么 |
| --- | --- |
| [`curl.sh`](./curl.sh) | 最小可用：OpenAI 兼容 + 流式 |
| [`python.py`](./python.py) | OpenAI Python SDK（对话 + 生图） |
| [`node.mjs`](./node.mjs) | OpenAI Node SDK（GPT 6 系记得用 `max_completion_tokens`） |
| [`anthropic.py`](./anthropic.py) | Anthropic `/v1/messages` 形状（Claude Code 用的就是这条） |
| [`gemini.sh`](./gemini.sh) | Gemini `v1beta generateContent` 形状 |
| [`claude-code.md`](./claude-code.md) | Claude Code 的 `~/.claude/settings.json` 配置 |
| [`codex.md`](./codex.md) | Codex CLI 的 `~/.codex/config.toml` 配置 |
| [`cherry-studio.md`](./cherry-studio.md) | Cherry Studio：对话 + 绘画（生图）配置 |

跑之前先确认：

```bash
export TOKEN=sk-...        # 控制台建的令牌
curl -s https://yydsrouter.com/v1/models -H "Authorization: Bearer $TOKEN" | head -c 200
```

能列出模型，说明令牌和网络都没问题。
