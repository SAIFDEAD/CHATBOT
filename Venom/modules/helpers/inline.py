from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Venom import OWNER
from Venom import VenomX

DEV_OP = [
    [
        InlineKeyboardButton(text=" 𝐎ᴡɴᴇʀ 🥀", user_id=OWNER),
        InlineKeyboardButton(text="𝐒ᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="•─╼⃝𖠁 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ 𖠁⃝╾─•",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text=" 𝐇ᴇʟᴘ & 𝐂ᴍᴅs 🚀", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text=" 𝐒ᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
        InlineKeyboardButton(text="𝐀ʙᴏᴜᴛ 🍂", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="•─╼⃝𖠁 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ 𖠁⃝╾─•",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text=" 𝐂ʟᴏsᴇ ✨",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text=" 𝐁ᴀᴄᴋ ✨", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text=" 𝐒ᴜᴋᴜɴᴀ 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="𝐓ᴏᴏʟs 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text=" 𝐁ᴀᴄᴋ ✨", callback_data="BACK"),
        InlineKeyboardButton(text=" 𝐂ʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="𝐂ʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="𝐄ɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="𝐃ɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="𝐌ᴜsɪᴄ 🌻", url=f"https://t.me/HINATA_N_BOT"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text=" 𝐁ᴀᴄᴋ 🐳", callback_data="SBACK"),
        InlineKeyboardButton(text="𝐂ʟᴏsᴇ 🌲", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text=" 𝐁ᴀᴄᴋ ✨", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(txt="𝐂ʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text=" 𝐇ᴇʟᴘ 🚀", callback_data="HELP"),
        InlineKeyboardButton(text=" 𝐂ʟᴏsᴇ 🐳", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text=" 𝐇ᴇʟᴘ 🚀", url=f"https://t.me/{VenomX.username}?start=help"
        ),
        InlineKeyboardButton(text=" 𝐂ʟᴏsᴇ 🐳", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="𝐒ᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="𝐇ᴇʟᴘ 🚀", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="𝐎ᴡɴᴇʀ 🍾", user_id=OWNER),
        InlineKeyboardButton(text=" 𝐒ᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text=" 𝐔ᴘᴅᴀᴛᴇs 🐳", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text=" 𝐁ᴀᴄᴋ ✨", callback_data="BACK"),
    ],
]
