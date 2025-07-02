import gspread
import datetime
from config import SHEET_URL, GS_CREDENTIALS_FILE

def save_reminder_to_sheet(user_id, reminder_time, user_name=None, level="free"):
    gc = gspread.service_account(filename=GS_CREDENTIALS_FILE)
    sh = gc.open_by_url(SHEET_URL)
    try:
        ws = sh.worksheet("reminders")  # 指定工作表
    except gspread.exceptions.WorksheetNotFound:
        ws = sh.add_worksheet(title="reminders", rows=100, cols=5)
        ws.append_row(["user_id", "reminder_time", "user_name", "level", "last_update"])

    now = datetime.datetime.now().strftime("%Y/%m/%d")
    user_id = str(user_id)
    records = ws.get_all_values()

    # 先檢查是否已經存在該 user_id
    updated = False
    for idx, row in enumerate(records[1:], start=2):  # 跳過表頭, Sheet從第2行
        if row[0] == user_id:
            ws.update(f"B{idx}:E{idx}", [[reminder_time, user_name or "", level, now]])
            updated = True
            break

    if not updated:
        ws.append_row([user_id, reminder_time, user_name or "", level, now])
