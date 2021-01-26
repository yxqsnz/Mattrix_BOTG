import discord
import aiohttp
import main,random
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
gifs= ["https://cdn.discordapp.com/attachments/798545214532878379/801857480585904148/gif.gif","https://cdn.discordapp.com/attachments/798545214532878379/801858297962823740/gife.gif","https://cdn.discordapp.com/attachments/798545214532878379/801858505639723008/gifi.gif"]
@commands.command(description='Da um tapa em alguém',brief='Da um tapa em alguém',)
async def tapa(ctx,Member:discord.Member=None):
    pass
    if Member == None:
        await ctx.send("Uso : tapa @usuário")
        return
    tapaembed = discord.Embed(title="Tapa Na Goxtosa",
     description=f"{ctx.author.mention} Deu um tapa em {Member.mention}",
     color=0xff0000,
     )
    tapaembed.set_thumbnail(url=ctx.author.avatar_url)
    tapaembed.set_image(url=random.choice(gifs))
    await ctx.send(embed=tapaembed)
def setup(bot):
    bot.add_command(tapa)