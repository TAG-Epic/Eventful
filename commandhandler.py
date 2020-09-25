"""
Created by Epic at 9/24/20
"""
from speedcord import Client
from speedcord.ext.typing import context


class CommandHandler:
    def __init__(self, client: Client, prefix: str):
        self.client = client
        self.prefix = prefix
        self.message_handlers = []
        self.command_handlers = {}

    async def handle_message(self, data):
        message = context.MessageContext(self.client, data)
        for message_handler in self.message_handlers:
            await message_handler(message)

        if message.content.startswith(self.prefix):
            command_message = CommandMessage(self, message)
            command = self.command_handlers.get(command_message.command)
            if command is None:
                return  # TODO: Maybe do a command not found message?
            await command(command_message)


class CommandMessage:
    def __init__(self, command_handler: CommandHandler, message_context):
        self.client = command_handler.client
        self.command_handler = command_handler
        self.message = message_context
        self.content = self.message.content[len(command_handler.prefix):]
        self.args = self.content.split(" ")
        self.command = self.args.pop(0)
