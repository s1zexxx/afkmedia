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

import config

# Get it from my.telegram.org
API_ID = int(getenv("23786230"))
API_HASH = getenv("c3a267db65847bfff3177db9084506ef")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("6156507750:AAF2xOZ_TwpugamOL1nXYnsTqw3BQk-r7Sw")
