from discord import Emoji
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.guild import Guild
from asyncio import sleep
from  main import bot
@commands.command()
async def emojis(ctx:Context):
    emojis = []
    total_send = 0
    e = 803400950894428231
    paperplane = bot.get_emoji(id=e)
    sv:Guild = ctx.guild
    gn = sv.name
    await ctx.message.add_reaction(paperplane)
    for emoji in await sv.fetch_emojis():
        emojis.append(emoji)
    for emoji in emojis:
       total_send += 1
       await ctx.author.send(f"Emoji {total_send} de {len(emojis)} de {gn}")
       await ctx.author.send(f"{emoji}")
       
       await sleep(1)
    pass
def setup(bot):
    bot.add_command(emojis)