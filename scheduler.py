import analyzer

def daily_summary():
    summary = analyzer.get_today_summary()
    print(summary)  # 或未來改成發 Telegram

if __name__ == "__main__":
    daily_summary()