from discord import TextChannel,Embed
from discord.ext import commands
import json
@commands.command()
@commands.has_permissions(administrator=True)
async def cmdchannel(ctx,channel:TextChannel):
    try:
        f = open(f'./data/config/{ctx.guild.id}.json')
    except FileNotFoundError:
        f = open(f"./data/config/{ctx.guild.id}.json",'w')
        a = {}
        json.dump(a,f)
        f.close()
    f = open(f"./data/config/{ctx.guild.id}.json",'w')
    e = Embed(color=0x00ff00)
    e.title = "Aguarde..."
    e.set_author(icon_url=ctx.author.avatar_url,name=ctx.author.display_name)
    e.description = "Processando solicitação..."
    m = await ctx.send(embed=e)
    a = {
        "cmdchannel":f"{channel.id}"
    }
    json.dump(a,f)
    e.title = "Ok!"
    e.description = f"Canal de comandos alterado para <#{channel.id}>"
    await m.edit(embed=e)
def setup(bot):
    bot.add_command(cmdchannel)