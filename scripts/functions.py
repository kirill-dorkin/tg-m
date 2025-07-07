import asyncio
from datetime import datetime
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import gspread

from config.telegram import API_ID, API_HASH

debug = False


def send_message(sender_session, receiver, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    if debug:
        print(f'Message {message} sent to {receiver} at {datetime.now()} from {sender_session=}')
        return True

    client = TelegramClient(StringSession(sender_session),
                            API_ID, API_HASH, loop=loop)

    client.connect()
    try:
        client.send_message(receiver, message)
        client.disconnect()
        return True
    except Exception as e:
        client.disconnect()
        return False


def join_grp(grp_name, str_sess):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient(StringSession(str_sess), API_ID, API_HASH, loop=loop)
    with client:
        try:
            client(JoinChannelRequest(grp_name))
            return True
        except:
            return False

def get_gspread(url,filename="scripts/cred.json"):
    gc = gspread.service_account(filename=filename)
    gsheet = gc.open_by_url(url)
    return gsheet
    


def fetch_messages_gspread(url,sheet_no,starting_row,ending_row,names_col,messages_col):
    gsheet = get_gspread(url)
    worksheet = gsheet.get_worksheet(sheet_no-1)
    
    names = worksheet.col_values(names_col)[starting_row:ending_row]
    messages = worksheet.col_values(messages_col)[starting_row:ending_row]
    return names,messages

