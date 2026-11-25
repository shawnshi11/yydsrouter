# Claude Code 接入

Claude Code 说的是 Anthropic 协议（`/v1/messages`），所以只需要把 base URL 指过来。

## 1. 写配置

`~/.claude/settings.json`：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://yydsrouter.com",
    "ANTHROPIC_AUTH_TOKEN": "sk-...",
    "ANTHROPIC_MODEL": "claude-haiku-5.5",
    "ANTHROPIC_SMALL_FAST_MODEL": "claude-haiku-5.5",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
  }
}
```

- **base URL 不要带 `/v1`**：Claude Code 自己会拼 `/v1/messages`。
- `ANTHROPIC_MODEL` 填网关里的模型名（`claude-sonnet-5.5`、`claude-opus-5.5` 等），想换模型直接改这里或用 `--model`。

## 2. 验证

```bash
claude -p "只回两个字：收到" --max-turns 1 --model claude-haiku-5.5 --output-format json
```

返回里 `result` 是「收到」就通了。实测一轮 `-p` 大约 1.8 万输入 token（其中大部分会命中提示缓存）、
输出几个 token，单次成本极低。

## 3. 注意

- Claude Code 会带 `cache_control` 做提示缓存，网关原样透传——第二轮的缓存读会让输入成本大幅下降。
- 工具调用（Bash / Read / Edit）走标准 function calling，实测可用。
