import os
import logging
import yaml

from telethon import TelegramClient


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = int(os.getenv('API_ID', CONFIG['api_id']))
API_HASH = os.getenv('API_HASH', CONFIG['api_hash'])
DUMP_ID = os.getenv('DUMP_ID', CONFIG['dump_id'])
TOKEN = os.getenv('TOKEN', CONFIG['TOKEN'])

Ubot = TelegramClient('Ubot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
