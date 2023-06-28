#
# Copyright (C) 2021-2022 by Teams1zex@Github, < https://github.com/Teams1zex >.
#
# This file is part of < https://github.com/Teams1zex/s1zexAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Teams1zex/s1zexAFKBot/blob/master/LICENSE >
#
# All rights reserved.


import asyncio
import importlib

from pyrogram import idle

from s1zex.modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def initiate_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("s1zex.modules." + all_module)
    print("Started s1zex AFK Bot.")
    await idle()
    print("GoodBye! Stopping Bot")


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
