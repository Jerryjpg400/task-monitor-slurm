import sys
from telegram import Bot
from telegram.constants import ParseMode
from .config import BOT_TOKEN, CHAT_ID

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)


async def send_telegram_message(message: str) -> None:
    """
    Sends a message to the specified Telegram chat.

    Args:
        message (str): The message to send.
    """
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Error sending Telegram message: {e}", file=sys.stderr)

