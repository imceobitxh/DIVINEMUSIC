from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓ¢σмє ƒσя Spartan Friend ✪
 
 ➲ Sab Matlabi Hai ✰
 
 ➲ But Sab Op Hai ✰
 
 ➲ 24x7 Active rhta ha  ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("Repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ADD ME", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("SPARTAN", url="https://t.me/XdLover_05"),
          InlineKeyboardButton("LUCKY", url="https://t.me/@Ihate0000000000"),
          ],
               [
                InlineKeyboardButton("MAYRA", url="https://t.me/unfairwrlxd"),

],
[
              InlineKeyboardButton("MISUKI", url=f"https://t.me/itz_misuki"),
              InlineKeyboardButton("︎FIDA", url=f"https://t.me/ll_Fida_Op_ll"),
              ],
              [
              InlineKeyboardButton("SHARIF", url=f"https://t.me/StatusWorld_05"),
InlineKeyboardButton("JORDAN", url=f"https://t.me/Syed0002"),
],
[
InlineKeyboardButton("HINATA", url=f"https://t.me/pretty_vaishu_xd"),
InlineKeyboardButton("SWEETY", url=f"https://t.me/unfairwrlxd"),
],
[
              InlineKeyboardButton("AAYU", url=f"https://t.me/ll_aayu_01l"),
              InlineKeyboardButton("MISJHA", url=f"https://t.me/Eye_killer12"),
              ],
              [
              InlineKeyboardButton("ZIYA", url=f"Bhatakti_aatma05"),
InlineKeyboardButton("MASUM", url=f"https://t.me/II_pagal_II"),
],
[
InlineKeyboardButton("AHL-E-ISHQ", url=f"https://t.me/StatusWorld_05"),
InlineKeyboardButton("MUSIC", url=f"https://t.me/XdMusic_Bot"),
],
[
InlineKeyboardButton("MISS-XD", url=f"https://t.me/Vickmachine05_Bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/fa4d23ef8b010a7b40d56.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("Repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://github.com/Danishzain05/ChatgptMusic")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/Danishzain05/ChatgptMusic) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/SpartanWorld_05)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


