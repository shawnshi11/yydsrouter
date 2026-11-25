#!/usr/bin/env bash
# Gemini 原生形状（v1beta generateContent）：Google SDK / curl 都走这条。
set -euo pipefail
TOKEN="${TOKEN:?先 export TOKEN=sk-...}"

curl -s "https://yydsrouter.com/v1beta/models/gemini-4-hydrogen:generateContent" \
  -H "x-goog-api-key: $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "只回两个字：收到"}]}],
    "generationConfig": {"maxOutputTokens": 200}
  }'
