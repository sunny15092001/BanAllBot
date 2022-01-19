from pyrogram import Client,filters
import logging
import os

class Config:
    TELEGRAM_TOKEN=os.environ['TELEGRAM_TOKEN']
    TELEGRAM_APP_HASH=os.environ['TELEGRAM_APP_HASH']
    TELEGRAM_APP_ID=int(os.environ['TELEGRAM_APP_ID'])
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(
           ":memory:",
           api_id=Config.TELEGRAM_APP_ID,
           api_hash=Config.TELEGRAM_APP_HASH,
           bot_token=Config.TELEGRAM_TOKEN
)
