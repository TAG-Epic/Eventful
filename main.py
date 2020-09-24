"""
Created by Epic at 9/24/20
"""
from speedcord import Client
from speedcord.ext.typing.context import MessageContext
from os import environ as env

bot = Client(640)

bot.token = env["TOKEN"]

bot.run()
