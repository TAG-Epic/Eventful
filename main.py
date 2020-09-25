"""
Created by Epic at 9/24/20
"""
from speedcord import Client
from os import environ as env
import commands
import commandhandler

bot = Client(640)
bot.command_handler = commandhandler.CommandHandler(bot, env["PREFIX"])

# Register commands
bot.command_handler.command_handlers["help"] = commands.help_command


@bot.listen("MESSAGE_CREATE")
async def on_message(data, shard):
    print("Got message")
    await bot.command_handler.handle_message(data)


bot.token = env["TOKEN"]

bot.run()
