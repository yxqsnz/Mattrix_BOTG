from discord.ext import commands
from discord.ext.commands import has_permissions

@commands.command(aliases=['prune','purge'])
@has_permissions(administrator=True)
async def clear(ctx,toclear:str = "10"):
  if not toclear.isnumeric():
      await ctx.send(":x:| Somente números são permitidos!")
      return
  toclear = int(toclear)
  await ctx.channel.purge(limit=toclear)
  await ctx.send(f":white_check_mark:| O chat teve {toclear} Mensagens deletadas.")
def setup(bot):
    bot.add_command(clear)