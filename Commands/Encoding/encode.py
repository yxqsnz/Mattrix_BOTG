import Scripts.hashgenerator
import Scripts.base64MGR
from discord.ext import commands


@commands.command()
async def encode(ctx,arg1="",*,args=""):
    pass
    if(arg1 == False or arg1==""):
        await  ctx.reply("USO `m!encode <md5/md10/B64-decode/B64-encode> texto.comq`")
    else:
        if args == "" and arg1:
            await ctx.reply(f"USO: `m!encode {arg1} texto`")
        if (arg1 == "md5" and args):
            await ctx.reply(f"Aqui está: {Scripts.hashgenerator.GenHashmd5(args)}")
        elif (arg1 == "md10" and args):
            await ctx.reply(f"Aqui está: {Scripts.hashgenerator.GenHashmd10(args)}")
        elif arg1 == "B64-encode" and args:
            await ctx.reply(f"Aqui está: {Scripts.base64MGR.EncodeB64(args)}")
        elif arg1 == "B64-decode" and args:
            await ctx.reply(f"Aqui está: {Scripts.base64MGR.DecodeB64(args)}")
        else:
            await ctx.reply(f"Codificação invalida!")
def setup(bot):
    bot.add_command(encode)