import gspread
import datetime
from config import SHEET_URL, GS_CREDENTIALS_FILE

def classify(text: str) -> str:
    text = text.lower()
    if "吃" in text or "餐" in text:
        return "飲食"
    elif "運動" in text or "跑" in text:
        return "運動"
    elif "睡" in text or "早起" in text:
        return "作息"
    else:
        return "其他"

def log_to_sheet(category, text):
    gc = gspread.service_account(filename=GS_CREDENTIALS_FILE)
    sh = gc.open_by_url(SHEET_URL)
    worksheet = sh.sheet1
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    worksheet.append_row([category, text, now])
