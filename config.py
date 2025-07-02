import os
from dotenv import load_dotenv
import json

# 本地開發讀取 .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SHEET_URL = os.getenv("SHEET_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Google 憑證自動寫入
GS_CREDENTIALS_FILE = os.getenv("GS_CREDENTIALS_FILE", "leimai-v0-6c91b6b47766.json")
GS_CREDENTIALS_JSON = os.getenv("GS_CREDENTIALS_JSON")

if GS_CREDENTIALS_JSON and not os.path.exists(GS_CREDENTIALS_FILE):
    with open(GS_CREDENTIALS_FILE, "w", encoding="utf-8") as f:
        f.write(GS_CREDENTIALS_JSON)
