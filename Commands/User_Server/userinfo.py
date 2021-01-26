import discord
from discord.ext import commands
@commands.command(aliases=["uinfo"],brief="mostra as infomacoes do usuario")
async def userinfo(ctx,Member:discord.Member=None):
   if Member == None:
       Member = ctx.author
   userinfoembed = discord.Embed(
       title="Informaçoes de Usuario",
       color=0x011021,
   )
   uroles= ""
   ac= "Nenhum"
   for role in Member.roles:
       uroles += str(role) +"\n"
   for acg in Member.activities:
       if acg:
        ac =""
        ac += str(acg) + "\n"
   userinfoembed.set_thumbnail(url=Member.avatar_url)
   userinfoembed.add_field(name=":newspaper2:Cargos: ",value=uroles)
   userinfoembed.add_field(name=":door:Entrou em: ", value=str(Member.joined_at)[:19])
   userinfoembed.add_field(name=":door:Conta criada em: ", value=str(Member.created_at)[:19])
   userinfoembed.add_field(name=":on:Está Online : ",value=Member.raw_status)
   userinfoembed.add_field(name=":scroll:Atividades: ",value=ac)
   userinfoembed.add_field(name=":id:ID: ",value=Member.id)
   userinfoembed.add_field(name=":shield:Perms: ",value=str(Member.guild_permissions.value))
   userinfoembed.add_field(name=":rainbow_flag:Cor: ",value=str(Member.color))
   
   await ctx.send(embed=userinfoembed)
   
def setup(bot):
    bot.add_command(userinfo)