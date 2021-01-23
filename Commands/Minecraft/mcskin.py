import discord
from MojangAPI import Client
from discord.ext import commands
@commands.command()
async def mcskin(ctx,arg=None):
    if arg == None:
        await  ctx.send("Uso: mcskin <nomedeusuariominecraft>")
        return
    m = await ctx.send("Aguarde...")
    skinEmbed = discord.Embed(
        title="McSkin",
        color = 0x00ff00
    )
    user = await Client.User.createUser(arg)
    profile = await user.getProfile()
    skinEmbed.set_footer(text="Powered By MojangAPI")
    skinEmbed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    skinEmbed.add_field(name="Skin de:",value=arg) 
    skinEmbed.set_image(url=profile.skin)
    await m.edit(content="Pronto!",embed=skinEmbed)
   
    pass
def setup(bot):
    bot.add_command(mcskin)