from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("INSERT YOUR API KEY-->"))
API_HASH = input("INSERT YOUR API HASH-->") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
TOKEN = bot.session.save()
print(TOKEN)
