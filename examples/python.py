"""OpenAI SDK 直连：只改 base_url 和 api_key，其他一行不动。"""
import os

from openai import OpenAI

client = OpenAI(base_url="https://yydsrouter.com/v1", api_key=os.environ["TOKEN"])

stream = client.chat.completions.create(
    model="claude-haiku-5.5",
    max_tokens=64,
    messages=[{"role": "user", "content": "只回两个字：收到"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
print()

# 生图：1K + low 是最便宜的一档；2.5 系只有约 1024，2.6 系才有 2K/4K。
import base64

image = client.images.generate(
    model="gpt-image-2.6-sunburst",
    prompt="超写实人像，穿米色风衣的年轻女性，傍晚旧城石板街，黄金时刻逆光，35mm，8K",
    extra_body={"resolution": "1K", "quality": "low"},
)
open("out.png", "wb").write(base64.b64decode(image.data[0].b64_json))
