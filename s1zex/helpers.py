#
# Copyright (C) 2021-2022 by Teams1zex@Github, < https://github.com/Teams1zex >.
#
# This file is part of < https://github.com/Teams1zex/s1zexAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Teams1zex/s1zexAFKBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio

from typing import Union
from datetime import datetime, timedelta
from s1zex import cleanmode, app, botname
from s1zex.database import is_cleanmode_on
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


async def put_cleanmode(chat_id, message_id):
    if chat_id not in cleanmode:
        cleanmode[chat_id] = []
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=5),
    }
    cleanmode[chat_id].append(put)


async def auto_clean():
    while not await asyncio.sleep(30):
        try:
            for chat_id in cleanmode:
                if not await is_cleanmode_on(chat_id):
                    continue
                for x in cleanmode[chat_id]:
                    if datetime.now() > x["timer_after"]:
                        try:
                            await app.delete_messages(chat_id, x["msg_id"])
                        except FloodWait as e:
                            await asyncio.sleep(e.x)
                        except:
                            continue
                    else:
                        continue
        except:
            continue


asyncio.create_task(auto_clean())


RANDOM = [
    "https://te.legra.ph/file/c3f7696d03d6a9c16f20d.jpg,"
    "https://te.legra.ph/file/03f5f05eaa5852b55f722.jpg,"
    "https://te.legra.ph/file/e7661805b3df6d132e07f.jpg,"
    "https://te.legra.ph/file/908885dde1bf6e91057cd.jpg,"
    "https://te.legra.ph/file/674f42f3dde303b844dd2.jpg,"
    "https://te.legra.ph/file/69696001a2e4b6ec74721.jpg,"
    "https://te.legra.ph/file/634f56d54b378783aec7b.jpg,"
    "https://te.legra.ph/file/8049f882528c125d30c68.jpg,"
    "https://te.legra.ph/file/ddc65c2492215c6eabab9.jpg,"
    "https://te.legra.ph/file/c3e93ea21a6f581d6ff35.jpg,"
    "https://te.legra.ph/file/d7db348e73fcf611f822f.jpg,"
    "https://te.legra.ph/file/9ec3409e093cbaf24331d.jpg,"
    "https://te.legra.ph/file/11a816b0eca4cdf8479b2.jpg,"
    "https://te.legra.ph/file/ddc65c2492215c6eabab9.jpg,"
    "https://te.legra.ph/file/a12bd8ca1dde7286e005c.jpg,"
    "https://te.legra.ph/file/a6ceb30aed67182e3459a.jpg,"
    "https://te.legra.ph/file/c9a5b632ba44a1fd0ceef.jpg,"
    "https://te.legra.ph/file/99c938c0a73df22eeb235.jpg,"
    "https://te.legra.ph/file/612579314592b65d62f3e.jpg,"
    "https://te.legra.ph/file/1ef45675b53eefa20ae6d.jpg,"
    "https://te.legra.ph/file/b701b4f0f3abfc0df16ad.jpg,"
    "https://te.legra.ph/file/31658015bdfedebbfe135.jpg,"
    "https://te.legra.ph/file/36a7155f4c4da0d3e900d.jpg,"
    "https://te.legra.ph/file/7f8aa5918c47564072ca3.jpg,"
    "https://te.legra.ph/file/b0fe14e4e203bb25ac6e6.jpg,"
    "https://te.legra.ph/file/b1c5506d0572e38c5ffc4.jpg,"
    "https://te.legra.ph/file/007747d2b1ac04ec5e26e.jpg,"
    "https://te.legra.ph/file/966d5dc26d5ecd8d45902.jpg,"
    "https://te.legra.ph/file/91ba23f7a5c5224d95539.jpg,"
    "https://te.legra.ph/file/6195a5d95c615375a6aa8.jpg,"
    "https://te.legra.ph/file/005fde01b399555585487.jpg,"
    "https://te.legra.ph/file/6c9d26d6b12cfc6d133b4.jpg,"
    "https://te.legra.ph/file/895b01520435b99debb72.jpg,"
    "https://te.legra.ph/file/485f46dd56c96330ea701.jpg,"
    "https://te.legra.ph/file/ded2d034c8ff002e54f73.jpg,"
    "https://te.legra.ph/file/afef890bbdee6496b22a4.jpg,"
    "https://te.legra.ph/file/142850ce85f31db9ecf7a.jpg,"
    "https://te.legra.ph/file/d874ae891d7c8299af56e.jpg,"
    "https://te.legra.ph/file/b5aa94cb462864ec58b4b.jpg,"
    "https://te.legra.ph/file/54f407a40bb8b35f46b76.jpg,"
    "https://te.legra.ph/file/b81aec1d7d6df382249d2.jpg,"
    "https://te.legra.ph/file/7ad483dccf95fedc7555d.jpg"

]


HELP_TEXT = f"""Добро пожаловать {botname}'s здесь помощь

- AFK he


/afk - This will set you offline.

/afk [Reason] - This will set you offline with a reason.

/afk [Replied to a Sticker/Photo] - This will set you offline with an image or sticker.

/afk [Replied to a Sticker/Photo] [Reason] - This will set you afk with an image and reason both.


/settings - To change or edit basic settings of AFK Bot.
"""

def settings_markup(status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="🔄 Clean Mode", callback_data="cleanmode_answer"),
            InlineKeyboardButton(
                text="✅ Enabled" if status == True else "❌ Disabled",
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons
