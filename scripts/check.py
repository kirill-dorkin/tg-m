from telethon import TelegramClient
from telethon.sessions import StringSession

from config.telegram import API_ID, API_HASH, SESSION_STRING

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH, sequential_updates=True)


async def main():
    print(await client.get_me())


with client:
    client.loop.run_until_complete(main())
