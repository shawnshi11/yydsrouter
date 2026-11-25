# Cherry Studio 接入（对话 + 绘画）

Cherry Studio 一个服务商就能同时做对话和生图，但要**把模型的「用途」改成图像生成**，否则它只当聊天模型。

## 1. 加服务商

设置 → 模型服务 → **添加**：

| 字段 | 值 |
| --- | --- |
| 提供商名称 | `YYDS Router` |
| 提供商类型 | `OpenAI`（OpenAI 兼容） |
| API 地址 | `https://yydsrouter.com/v1`（若客户端自动补 `/v1` 导致出现 `/v1/v1`，就只填域名） |
| API 密钥 | `sk-...` |

## 2. 加模型

点「获取模型列表」，或者手动添加：

- 对话：`claude-sonnet-5.5`、`gpt-6.2-sol`、`gemini-4-argon` 之类
- 绘画：`gpt-image-2.6-sunburst`（写实）、`gpt-image-2.6-flare`（艺术感）

**关键一步**：把绘画模型的「用途」从默认改成 **图像生成**，否则绘画页里选不到它。

## 3. 出图

左侧「绘画」→ 选模型 → 填提示词。客户端一般只传 `size`，网关会按长边映射档位（`1024x1024` → 1K），
**不传 `quality` 时按最低档计价**（同档位里 2.5 系比 2.6 系便宜）。

要 2K/4K 或指定画质，用脚本调（客户端未必透传这些参数）：

```bash
curl -s https://yydsrouter.com/v1/images/generations \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"model":"gpt-image-2.6-sunburst","prompt":"傍晚的石板街，黄金时刻逆光","resolution":"2K","quality":"medium"}'
```
