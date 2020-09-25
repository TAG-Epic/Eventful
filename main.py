"""
Created by Epic at 9/24/20
"""
from speedcord import Client
from os import environ as env
import commandhandler

bot = Client(640)
bot.command_handler = commandhandler.CommandHandler(bot, env["PREFIX"])


@bot.listen("MESSAGE_CREATE")
async def on_message(data, shard):
    await bot.command_handler.handle_message(data)


bot.token = env["TOKEN"]

bot.run()
