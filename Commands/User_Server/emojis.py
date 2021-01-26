from discord import Emoji,Embed,Forbidden
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.guild import Guild
from asyncio import sleep
from  main import bot
@commands.command(brief="Envia todos os emojis do server na sua DM!",description="Envia todos os emojis do server na sua DM!")
async def emojis(ctx:Context):
    emojis = []
    total_send = 0
    
    e = 803585399774511135
    paperplane = bot.get_emoji(id=e)
    sv:Guild = ctx.guild
    gn = sv.name
    await ctx.message.add_reaction(paperplane)
    for emoji in await sv.fetch_emojis():
        emojis.append(emoji)
    for emoji in emojis:
       total_send += 1
       em:Embed = Embed(
           title=f"Emoji {total_send} de {len(emojis)} de {gn}",
           
       )
       em.add_field(name="Nome: ",value=emoji.name,inline=False)
       em.add_field(name='id:',value=emoji.id,inline=False)
       em.set_image(url=emoji.url)
       em.set_author(icon_url=ctx.author.avatar_url,name=ctx.author.display_name)
       em.set_footer(text="Powered By Mattrix Bot")
       try:
        await ctx.author.send(embed=em)
       except Forbidden:
           await ctx.send('Envio cancelado.')
           return
       await sleep(1)
    pass
def setup(bot):
    bot.add_command(emojis)