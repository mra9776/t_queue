from telethon.sync import TelegramClient
from config import *

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
