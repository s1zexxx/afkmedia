#
# Copyright (C) 2021-2022 by Teams1zex@Github, < https://github.com/Teams1zex >.
#
# This file is part of < https://github.com/Teams1zex/s1zexAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Teams1zex/s1zexAFKBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
