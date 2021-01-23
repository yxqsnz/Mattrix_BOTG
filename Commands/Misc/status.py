import discord,math,time,os,psutil
import psutil,sys
from platform import platform
from main import bot
from main import *
#a
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = round( py.memory_info()[0]  / 1000000) # memory use in GB...I think
from main import client
@commands.command()
async def status(ctx):
    antes = time.monotonic()
    msg = await ctx.send(embed=discord.Embed(title="Aguarde...", description=f"Isso pode demorar um pouco....", color=0xFF5733))


    api_ping = float(str(bot.latency)[2:5])
    bot_ping = round((time.monotonic() - antes) * 1000)
    bot_api_ping_good_emoji = bot.get_emoji(id=802301224539652147)
    bot_ping_medium_emoji = bot.get_emoji(id=802301264809164820)
    bot_ping_bad_emoji = bot.get_emoji(id=802301247734546482)
    emoji_api_sel = ""
    def sel_api_ping_emoji(ping):
        if ping >= 250:
             return bot_ping_bad_emoji
        elif ping <= 250 and ping > 150:
             return bot_ping_medium_emoji
        else:
             return bot_api_ping_good_emoji
    emoji_api_sel = sel_api_ping_emoji(api_ping)
    emoji_bot_ping_sel = sel_api_ping_emoji(bot_ping)
    embed=discord.Embed(title="Status!", description=f"HOST-CPU-USAGE: {psutil.cpu_percent()}%\nHOST-RAM-USAGE: {psutil.virtual_memory().used / 1000000 :.2f}MB {psutil.virtual_memory().percent}% \nBOT-RAM-USAGE: {memoryUse}MB\nAPI-PING: {emoji_api_sel} > {api_ping}MS\nBOT-PING: {emoji_bot_ping_sel} > {bot_ping}MS\nOS: {platform()}\nVersão-do-python: {sys.version}", color=0xFF5733)
    embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
    embed.set_footer(text="yeah Boi")
    await msg.edit(embed=embed)
def setup(bot):
    
    bot.add_command(status)