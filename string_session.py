#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677 and SpEcHiDe
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details
Check your Telegram saved messages section to copy the STRING_SESSION"""
)
API_KEY = int(input("1301043: "))
API_HASH = input("f2f2cfb48fe1182b125064f4dede5c4e: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Check your Telegram Saved Messages to copy the STRING_SESSION value")
    session_string = client.session.save()
    saved_messages_template = """Support: @userbotindo

<code>STRING_SESSION</code>: <code>{}</code>

⚠️ <i>Please be carefull to pass this value to third parties</i>""".format(
        session_string
    )
    client.send_message("me", saved_messages_template, parse_mode="html")
