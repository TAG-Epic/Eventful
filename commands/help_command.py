"""
Created by Epic at 9/25/20
"""
from speedcord.ext.typing.context import MessageContext
import event_config

help_menus = {
    "virus": """
    **Virus outbreak!**
    __Basic explanation:__
    You have a random chance to infect someone who sent a message in the last 30s or when you are in a voice chat together
    You can buy corona test kit to label yourself as infected which will give you 1000 event coins and cure you if you are infected, but mute you for a random amount of time
    You can earn a small amount of coins by chatting
    
    **Commands**
    !help
    !test - Take the corona test (10 event coins)
    """
}


async def execute(context: MessageContext):
    await context.send(content=help_menus[event_config.ACTIVE_EVENT])
