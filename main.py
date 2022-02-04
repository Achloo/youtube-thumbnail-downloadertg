# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """

<b>Hello {},

I am a simple youtube thumbnail downloader telegram bot.</b>

- <code>Send a youtube video link or video ID.</code>

- <code>I will send the thumbnail.</code>

<b>Made by @razkidz</b>

"""

START_BUTTON = InlineKeyboardMarkup(

        [[

        InlineKeyboardButton('🗣️ Group', url='https://t.me/mallubotzofficial'),

        InlineKeyboardButton('📢 Channel', url='https://t.me/mallurockzofficial'),

        InlineKeyboardButton('📃 Bot List', url='https://t.me/mallurockzofficial/3')

        ],[

        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://youtube.com/channel/UCYmBtjtt94XAalZkmFZrYcw')

        ]]

    )

BUTTONS = InlineKeyboardMarkup(

        [[

        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://youtube.com/channel/UCYmBtjtt94XAalZkmFZrYcw')

        ]]

    )

REGEX = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

Bot = Client(

    "YouTube-Thumbnail-Downloader",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)

@Bot.on_message(filters.private & filters.command(["start"]))

async def start(bot, update):

    text = START_TEXT.format(update.from_user.mention)

    reply_markup = START_BUTTON

    await update.reply_text(

        text=text,

        disable_web_page_preview=True,

        reply_markup=reply_markup,

        quote=True

    )

@Bot.on_message(filters.private & filters.text)

async def send_thumbnail(bot, update):

    message = await update.reply_text(

        text="`Analysing...`",

        disable_web_page_preview=True,

        quote=True

    )

    if ("youtube.com" in update.text) and ("/" in update.text) and ("=" in update.text):

        id = update.text.split("=")[-1]

    elif ("youtu.be" in update.text) and ("/" in update.text):

        id = update.text.split("/")[-1]

    else:

        id = update.text

    try:

        thumbnail = "https://img.youtube.com/vi/" + id + "/sddefault.jpg"

        await update.reply_photo(

            photo=thumbnail,

            reply_markup=BUTTONS,

            quote=True

        )

        await message.delete()

    except Exception as error:

        await message.edit_text(

            text=error,

            disable_web_page_preview=True,

            reply_markup=BUTTONS

        )

Bot.run()
