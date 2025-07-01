# HealthTracker – AI 健康習慣追蹤助理

"""
版本：V0.1
目標：打造一個能記錄、分類、儲存、分析日常健康行為並提供建議，並具備訂閱制服務的 AI 助理
開發語言：Python
整合技術：Telegram Bot + Google Sheet + GPT API
"""

# TODO List（開發任務分階段）

# ✅ 第一階段：基礎日誌紀錄系統
# 1. 建立 Telegram Bot 並接收使用者訊息（已完成）
# 2. 將訊息分類為：飲食 / 運動 / 作息（使用簡單 if 條件）
# 3. 每筆訊息寫入 Google Sheet（使用 gspread）

# ⏳ 第二階段：每日提醒與資料蒐集
# 4. 用戶可自訂每日提醒時間，機器人主動推播訊息（一天一次）
# 5. 引導用戶使用「鍵盤選項」回答當日飲食與睡眠紀錄（幾餐 / 每餐內容 / 睡眠時數）

# 🔜 第三階段：週期性總結與回饋
# 6. 每週自動統整 7 天紀錄並傳送摘要
# 7. 呼叫 GPT API，根據過去一週的行為給出健康建議

# 🔮 第四階段：視覺化與長期習慣建模
# 8. 對每日 / 每週資料進行次數、比例、分佈分析
# 9. 使用 matplotlib / plotly 回傳圖像摘要
# 10. 建立個人化模型（行為偏好 / 時間選擇最佳化）

# 🟣 第五階段：訂閱機制與會員等級服務
# 11. 新增用戶訂閱管理模組（可綁定 Telegram / Email / 手機）
# 12. 不同等級（免費、進階、VIP）解鎖額外功能（如：更細緻的分析、高頻推播、個人專屬顧問等）
# 13. 支援用戶升級與付款（可先手動，後續可自動化）
# 14. 依會員等級切換服務權限，動態顯示對應功能選單
# 15. 後端可與 Stripe、綠界、Line Pay 等金流整合

# 📦 外部整合工具
# - OpenAI GPT-4 API
# - Telegram Bot API
# - Google Sheet API（可升級至 PostgreSQL / Firestore）
# - Stripe / 綠界 / Line Pay 金流

# 📁 專案結構
# /health-tracker
# ├── main.py                  # 主程式，負責接收訊息與觸發回應
# ├── config.py                # 儲存 token、sheet URL、API key 等設定值
# ├── tracker.py               # 處理訊息分類與寫入 Google Sheet 的邏輯
# ├── scheduler.py             # 每日提醒與每週總結的排程邏輯
# ├── analyzer.py              # 對資料進行統計分析與建議生成
# ├── membership.py            # 會員等級與訂閱管理模組
# ├── billing.py               # 金流整合（可選）
# └── utils.py                 # 常用小工具函數

# 接下來可由 main.py 開始逐步串接 Bot 功能與用戶資料追蹤模組
