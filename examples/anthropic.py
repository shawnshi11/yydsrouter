"""Anthropic 形状（/v1/messages）：Claude Code、Anthropic SDK 走的就是这条。"""
import os

import httpx

response = httpx.post(
    "https://yydsrouter.com/v1/messages",
    headers={
        "x-api-key": os.environ["TOKEN"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
    json={
        "model": "claude-haiku-5.5",
        "max_tokens": 64,
        "messages": [{"role": "user", "content": "只回两个字：收到"}],
    },
    timeout=60,
)
print(response.json()["content"][0]["text"])
