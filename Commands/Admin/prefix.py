from discord.ext import commands
from discord import Member,Permissions
from discord.ext.commands import has_permissions
import json

from discord.ext.commands.context import Context


@commands.command(brief="Muda o prefix do BOT",description="Muda o prefix do bot nesse servidor!",category="Administrador")
async def prefix(ctx:Context,*,prefix=None):
    
    with open('./data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

   
    if prefix == None:
        await ctx.send(f"O meu Prefixo nesse server é: `{prefixes[str(ctx.guild.id)]}`")
        return
   
    if  ctx.author.guild_permissions.administrator:
        prefixes[str(ctx.guild.id)] = prefix
        with open('./data/prefixes.json', 'w') as f: #writes the new prefix into the .json
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefixo Modificado para: `{prefix}`') #confirms the prefix it's been changed to  
    else:
        await ctx.send(f"Desculpe, {ctx.author.mention} Você não pode mudar meu prefixo nesse servidor!")

def setup(bot:commands.Bot):
    bot.add_command(prefix)
    