from discord.ext import commands
from discord import Guild,Embed,Emoji
from discord.ext.commands.context import Context
@commands.command()
async def emoji(ctx:Context,arg=None):
    if arg == None:
        await ctx.send("USO emoji <emoji>")
        return
    sv:Guild = ctx.guild
    semoji:Emoji = ""
    
    for emoji in await sv.fetch_emojis():
        if emoji.name == arg:
            semoji = emoji
            break
    if semoji == "":
        await ctx.send("Emoji invalido!")
        return
    e:Embed = Embed(
        title="Clique aqui para baixar o emoji",
        color=0xDEB76F,
        url=str(semoji.url)
    )
    e.set_image(url=str(semoji.url))
    
    e.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    await ctx.send(embed=e)
def setup(bot):
    bot.add_command(emoji)