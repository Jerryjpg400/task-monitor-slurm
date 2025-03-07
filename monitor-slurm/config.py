import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve Telegram bot credentials
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Ensure required environment variables are set
if not BOT_TOKEN or not CHAT_ID:
    print("Error: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set in the environment or .env file", file=sys.stderr)
    sys.exit(1)

