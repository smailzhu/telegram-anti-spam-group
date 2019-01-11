from configparser import ConfigParser

from telethon import TelegramClient, events

__author__ = 'smailzhu'

parser = ConfigParser()
parser.read('config.ini', encoding='utf-8')
api_id = int(parser.get('api', 'id'))
api_hash = parser.get('api', 'hash')
try:
    target_chat = int(parser.get('target', 'chat'))
except Exception:
    target_chat = parser.get('target', 'chat')

with TelegramClient('session_name', api_id, api_hash) as client:
    chat = client.get_entity(target_chat)


    @client.on(events.ChatAction(chats=target_chat))
    async def handler(event):
        if not event.user_added:
            return
        from_id = event.action_message.from_id
        msg = f"You have been invited by id: `{from_id}` to this spam group, " \
            "Please click report button above and forward this message to @HexJudge\n" \
            f"您已經被 id: `{from_id}` 給拉入到此騷擾群組，請點擊畫面上方回報來檢舉並轉傳此訊息至 @HexJudge"
        await event.reply(msg)


    client.start()
    client.run_until_disconnected()
    client.disconnect()
