import gspread
from config import SHEET_URL, GS_CREDENTIALS_FILE
import datetime

def get_today_summary():
    # 連接 Google Sheet
    gc = gspread.service_account(filename=GS_CREDENTIALS_FILE)
    sh = gc.open_by_url(SHEET_URL)
    worksheet = sh.sheet1
    records = worksheet.get_all_values()

    # 假設格式：[分類, 內容, 時間]
    today = datetime.datetime.now().strftime("%Y/%m/%d")
    summary = {}

    for row in records[1:]:  # 跳過表頭
        # 如果你已經有時間欄，抓 row[2]，否則略過這行檢查
        if len(row) >= 3 and row[2].startswith(today):
            category = row[0]
            summary[category] = summary.get(category, 0) + 1

    # 組合摘要文字
    lines = ["# 今日紀錄分類統計"]
    for category, count in summary.items():
        lines.append(f"- {category}：{count} 次")
    return "\n".join(lines)