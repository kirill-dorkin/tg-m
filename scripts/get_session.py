from telethon import TelegramClient
from telethon.sessions import StringSession

from config.telegram import API_ID, API_HASH

client = TelegramClient(StringSession(), API_ID, API_HASH, sequential_updates=True)


async def main():
    print(client.session.save())


with client:
    client.loop.run_until_complete(main())
