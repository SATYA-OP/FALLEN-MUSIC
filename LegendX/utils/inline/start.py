from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from LegendX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ð¥ð¼ADD ME TO YOUÆ¦ GÆ¦OUá´©ð¼ð¥",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ð¥ð¼Êá´Êá´ð¼ð¥",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="ð¥ð¼ê±á´á´á´ÉªÉ´É¢ê±ð¼ð¥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ð¥ð¼á´á´¡É´á´Êð¼ð¥", user_id=OWNER),
            InlineKeyboardButton(
                text="ð¥ð¼ê±á´á´á´á´Êá´ð¼ð¥", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ð¥ð¼ADD ME TO YOUÆ¦ GÆ¦OUá´©ð¼ð¥",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ð¥ð¼Êá´Êá´ð¼ð¥", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="ð¥ð¼á´á´ÉªÉ´á´á´ÉªÉ´á´Êð¼ð¥", user_id=OWNER),
            InlineKeyboardButton(
                text="ð¥ð¼ê±á´á´á´á´Êá´ð¼ð¥", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="ð¥ð¼ðððá´á´Êá´á´ á´á´á´á´ Êá´Êð¼ð¥ðð", url=f"https://t.me/ll_OFFICIAL_LEGENDBOY_ll"
                )
        ],
     ]
    return buttons
