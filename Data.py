# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
How to Use this Bot

  ❏ Commands for BOT Users
  ├ /start - Start Bot
  ├ /about - About this Bot
  ├ /help - Help this Bot Command
  ├ /ping - To check live bots
  └ /uptime - To view bot status
 
  ❏ Commands For BOT Admin
  ├ /logs - To view bot logs
  ├ /setvar - To set the var with the dibot command
  ├ /delvar - To delete var with dibot command
  ├ /getvar - To view one of the vars with the dibot command
  ├ /users - To view bot user statistics
  ├ /batch - To link more than one file
  ├ /speedtest - To test bot server speed
  └ /broadcast - To send broadcast messages to bot users

 👨‍💻 Powered by @ZenBotX
"""

    close = [
        [InlineKeyboardButton("↻ ᴄʟᴏsᴇ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("↻ ᴄʟᴏsᴇ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="about"),
            InlineKeyboardButton("↻ ᴄʟᴏsᴇ", callback_data="close")
        ],
    ]

    ABOUT = """
<b><u>About this Bot:</u></b>

 @{} is a Telegram Bot for saving Posts or Files that can be Accessed via a Special Link.

  • Creator: @ZenBotX
  • Framework: Pyrogram

 👨‍💻 Developed by @NoobZen
"""
