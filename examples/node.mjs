// OpenAI SDK（Node）：只改 baseURL 与 apiKey。
import OpenAI from 'openai'

const client = new OpenAI({
  baseURL: 'https://yydsrouter.com/v1',
  apiKey: process.env.TOKEN,
})

const stream = await client.chat.completions.create({
  model: 'gpt-6-luna',
  max_completion_tokens: 64, // GPT 6 系用 max_completion_tokens
  messages: [{ role: 'user', content: '只回两个字：收到' }],
  stream: true,
})

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? '')
}
