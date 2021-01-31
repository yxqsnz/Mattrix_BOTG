from discord.ext import commands
from main import bot
from datetime import datetime
from discord import Embed   
from discord.ext.commands.context import Context
@commands.command(brief="Reporta um bug",aliases=['reportar','rept'])
async def report(ctx:Context,tipo = None,*,args:str = None):
    t = Embed()
    t.title = "Aguarde..."
    t.description = "Enviando report..."
    t.set_author(icon_url=ctx.author.avatar_url,name=ctx.author.name)
    t.timestamp =  datetime.utcnow()
    t.color = 0xffff00
    if ctx.guild:
        await ctx.send("O Comando `report` só funciona em dm abra dm com o bot e use `dm! report <abuso/bug> <text>` !")
        return
    if tipo == None:
        await ctx.reply("Coloque o tipo do report! `dm! report <abuso/bug>`")
        return
    elif tipo.lower() == "abuso"  or tipo.lower() == "bug":
       pass
    else:
        await ctx.reply(f"o tipo: `{tipo}` é invalido!")
        return
    if args == None:
        await ctx.reply(f"Faltando argumento nessesario `m! report {tipo} <texto>`")   
        return 
    m = await ctx.send(embed=t)
    rp = await bot.fetch_channel(channel_id=803956161429766204)
    e:Embed = Embed()
    e.title = "Novo Report!"
    e.color = 0xff0000
    e.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
    e.add_field(name="ID: ", value=ctx.author.id)
    e.add_field(name="TIPO: ",value=tipo,inline=False)
    e.add_field(name="REPORT: ",value=args)
    e.timestamp = datetime.utcnow()
    await rp.send(embed=e)
    t = Embed()
    t.title = "Report Enviado!"
    t.description = "Ok!"
    t.color =  0x00ff00
    t.set_author(icon_url=ctx.author.avatar_url,name=ctx.author.name)
    t.timestamp =  datetime.utcnow()
    await m.edit(embed=t)
def setup(bot):
    bot.add_command(report)