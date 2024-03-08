from pyrogram import filters, Client
from pyrogram.types import Message

from Venom import OWNER, VenomX
from Venom.database.chats import get_served_chats
from Venom.database.users import get_served_users


@VenomX.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ sᴜᴋᴜɴᴀ ᴄʜᴀᴛʙᴏᴛ ɪs {(await cli.get_me()).mention} :

➻ **𝐂ʜᴀᴛs 𝐀ᴅᴅ 𝐒ᴜᴋᴀɴᴀ:** {chats}
➻ **𝐔sᴇʀs 𝐒ᴛᴀʀᴛᴇᴅ 𝐒ᴜᴋᴜɴᴀ:** {users}"""
    )
