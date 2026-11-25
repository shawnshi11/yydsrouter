#!/usr/bin/env bash
# 最小可用：OpenAI 兼容形状。把 TOKEN 换成控制台「API 密钥」里建的令牌。
set -euo pipefail
BASE="${BASE:-https://yydsrouter.com/v1}"
TOKEN="${TOKEN:?先 export TOKEN=sk-...}"

curl -s "$BASE/chat/completions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-haiku-5.5",
    "max_tokens": 64,
    "stream": true,
    "messages": [{"role": "user", "content": "只回两个字：收到"}]
  }'
