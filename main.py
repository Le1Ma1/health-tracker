from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN
from tracker import log_to_sheet, classify

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    category = classify(user_text)
    log_to_sheet(category, user_text)
    await update.message.reply_text(f"✅ 已記錄：{category}｜內容：「{user_text}」")

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("🤖 HealthTracker Bot is running...")
    app.run_polling()
