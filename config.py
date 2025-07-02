import os
from dotenv import load_dotenv

# 讀取本地 .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GS_CREDENTIALS_FILE = os.getenv("GS_CREDENTIALS_FILE")
SHEET_URL = os.getenv("SHEET_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
