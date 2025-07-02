from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from scheduler import start_set_reminder, handle_reminder_time

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("set_reminder", start_set_reminder))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_reminder_time))
    print("🤖 HealthTracker is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
