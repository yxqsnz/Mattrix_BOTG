from discord import Guild,Embed, embeds
from discord.ext import commands
from discord.ext.commands.context import Context
@commands.command(aliases=['sinfo','svinfo'])
async def serverinfo(ctx:Context):
    sv:Guild = ctx.guild
    e:Embed = Embed(
        title=f"Informaçoes de {sv.name}",
        color = 0x3242E5,
        description=f"Membros: {sv.member_count}\n \
                     Tem ícone animado: {sv.is_icon_animated()}\n \
                     Dono: <@{sv.owner_id}>\n \
                     Canais de Texto: {len(sv.text_channels)}\n \
                     Canais de audio: {len(sv.voice_channels)}\n   \
                     Emojis: {len(await sv.fetch_emojis())}\n \
                     Região: {str(sv.region).capitalize()}\n \
                     Total de Usuários que deram boost nesse server: {sv.premium_subscription_count}  \n  \
                     -end \n \
                     "
            
        
    )
    e.set_author(icon_url=ctx.author.avatar_url,name=ctx.author.display_name)
    e.set_thumbnail(url=sv.icon_url)
    await ctx.send(embed=e)
    
def setup(bot):
    bot.add_command(serverinfo)