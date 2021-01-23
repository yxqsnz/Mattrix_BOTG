import signal,os,random
import subprocess
from discord.ext import commands
from Scripts.utils import capturecmdexit,timeout,runJSScript
codeexit = ""
@commands.command()
async def runjsc(ctx, *, args):
    if "reboot" in args or 'rm -rf' in args or 'shutdown' in args or 'curl' in args or 'wget' in args or 'fr- mr' in args or '[::-1]' in args:
        await ctx.send(":shield: Ez Command Blocker\n codigo bloqueado!")
        return 
    rn = random.randint(0,ctx.author.id)
    args = str(args).replace("'",'"')
    os.system(f" cd /tmp/koderun;")
    f = open(f'script_{rn}.js','w')
    f.write(args)

    p = subprocess.check_output(['node', f'script_{rn}.js'])
    
    codeexit = p
    await ctx.send(p.decode('utf-8'))
    return
    os.system('rm -rf script_*.js')
    if codeexit.exitcode == 0:
        
            if len(codeexit.decode("utf-8")) <= 1955:
                await ctx.send(f'Saida do codigo:```\n{str(codeexit.stdout.decode("utf-8"))}``` ')
            else:
                await ctx.send(f'Saida do codigo:\n```{str(codeexit.stdout.decode("utf-8"))[:1955] + "..."}``` ')
    else:
        await ctx.send(f"Error: {codeexit.stderr}")
def setup(bot):
    bot.add_command(runjsc)
