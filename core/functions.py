import asyncio

from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest

from config.telegram import API_ID, API_HASH, SESSION_STRING


def get_uid(username):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH, loop=loop)
    with client:
        try:
            entity = client.get_entity(username)
            try:
                grp = entity.megagroup
                return {'group': entity.id}
            except AttributeError:
                return {'user': entity.id}
        except Exception as e:
            return e


def join_grp(grp_name):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH, loop=loop)
    with client:
        try:
            client(JoinChannelRequest(grp_name))
            return True
        except:
            return False
