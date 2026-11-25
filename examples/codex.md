# Codex CLI 接入

Codex 走 OpenAI 的 **Responses** 形状（`/v1/responses`），配置写在 `~/.codex/config.toml`。

## 1. 写配置

```toml
model_provider = "yyds"
model = "gpt-6.2-sol"          # 省钱可以先换 gpt-6-luna
model_reasoning_effort = "low"

[model_providers.yyds]
name = "YYDS Router"
base_url = "https://yydsrouter.com/v1"
env_key = "YYDS_API_KEY"
wire_api = "responses"
```

然后 `export YYDS_API_KEY=sk-...`（或者写进 shell profile）。

## 2. 验证

```bash
codex exec --skip-git-repo-check -c model="gpt-6-luna" "只回两个字：收到"
```

## 3. 注意

- **`gpt-6.2-sol` 一次空跑大约 1.2 万 token**（系统提示 + 工具定义 + 输出）。省钱就先 `gpt-6-luna`（与 Sol 的单价差约 20 倍）。
- Codex 会发 `store` / `metadata` / `seed` 之类的字段；网关对 GPT 6 系会过滤掉 `seed`（上游拒收它），其余原样透传。
- **Codex 内置的 `image_gen` 工具用不了**：那是 OpenAI 官方后端托管的工具，第三方网关没有。要生图用 `/v1/images/generations`（见 `python.py`）。
