from asyncio import sleep
from discord.ext import commands
from discord import Embed
from discord.ext.commands.core import command
@commands.command()
async def a(ctx):
    i = 0
    m = await ctx.send(i)
    for i in range(0,100):
        i += 1 
        await m.edit(content=f"{i} <@450812271451439124>")
        await sleep(1)  
    m.edit(content="<@450812271451439124> <@450812271451439124> <@450812271451439124> <@450812271451439124> <@450812271451439124> <@450812271451439124> <@450812271451439124><@450812271451439124> <@450812271451439124> <@450812271451439124> <@450812271451439124> <@450812271451439124> <@450812271451439124> <@450812271451439124> ")
def setup(bot):
    bot.add_command(a)