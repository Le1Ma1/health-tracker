import gspread
import datetime
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from config import SHEET_URL, GS_CREDENTIALS_FILE

# 可選時段列表
REMINDER_TIMES = [
    ["06:00", "07:00", "08:00"],
    ["09:00", "10:00", "11:00"],
    ["12:00", "13:00", "14:00"],
    ["15:00", "16:00", "17:00"],
    ["18:00", "19:00", "20:00"],
    ["21:00", "22:00", "自訂時間"]
]

async def start_set_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "請選擇每日提醒時間：",
        reply_markup=ReplyKeyboardMarkup(REMINDER_TIMES, one_time_keyboard=True, resize_keyboard=True)
    )

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

async def handle_reminder_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.full_name
    time_str = update.message.text.strip()
    all_choices = sum(REMINDER_TIMES, [])

    if time_str not in all_choices and time_str != "自訂時間":
        await update.message.reply_text("請從鍵盤選擇有效的時間")
        return

    if time_str == "自訂時間":
        await update.message.reply_text("請直接輸入你要的時間（例如 06:30）", reply_markup=ReplyKeyboardRemove())
        return

    # 呼叫寫入 Sheet
    save_reminder_to_sheet(user_id, time_str, user_name)
    await update.message.reply_text(
        f"✅ 已設定每天 {time_str} 提醒\n之後你會在這個時間收到健康問卷",
        reply_markup=ReplyKeyboardRemove()
    )
