import signal

from discord.ext import commands
from Scripts.utils import capturecmdexit,timeout
codeexit = ""


@commands.command(aliases=['rpyc'],brief="Roda um código em python")
async def runpyc(ctx, *, args):
    if "reboot" in args or 'rm -rf' in args or 'shutdown' in args or 'curl' in args or 'wget' in args or 'fr- mr' in args or '[::-1]' in args:
        await ctx.send(":shield: Ez Command Blocker\n codigo bloqueado!")
        return 
    args = args.replace("'",'"')
    codeexit = capturecmdexit(f" cd /tmp/koderun;python -c '{args}'")
    if str(type(codeexit)) == "<class 'str'>":

        if len(codeexit) <= 1955:
            await ctx.send(f'Saida do código:```\n{str(codeexit)}``` ')
        else:
            await ctx.send(f'Saida do código:\n```{str(codeexit)[:1955] + "..."}``` ')
    elif isinstance(codeexit,TimeoutError) or codeexit == TimeoutError or str(type(codeexit)) == "<class 'multiprocessing.context.TimeoutError'>":
        await  ctx.send("[*]Info: tempo limite excedido")
    
def setup(bot):
    bot.add_command(runpyc)
