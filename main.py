from logging import exception
import discord,colorama,sys,json,typing,glob,os,time,psutil,random,asyncio
from discord.ext import commands
from discord.ext.commands import *
from Scripts.envcontroller import ReturnEnv as config
from Scripts.MemoryCleaner import InitMemCleaner
pid = os.getpid()
py = psutil.Process(pid)
print('Starting UP....')
os.system('rm -rf /tmp/koderun/')
time.sleep(0.1)
os.system('mkdir /tmp/koderun/')
def rtk():
    pass
#config = json.loads(config_t)
client = discord.Client()
bot = commands.Bot(command_prefix=config('PREFIX'))

started = time.perf_counter()
total_commands = 0
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele +"\n" 
    
    # return string   
    return str1  
commands_loaded=0
pcmds = []
def returncmds():
    return listToString(pcmds)
cmds:list = []
os.system('rm -rf __pycache__')
cmd_folders = []
for r,s,files in os.walk("./Commands"):
    for folders in s:
        cmd_folders.append(folders)
    for folder in cmd_folders:
       for file in os.listdir(f"./Commands/{folder}"):
         if file.endswith(".py"):
            command = file.replace('.py',"")
            cmds.append(command)
            for cmd in cmds:
                try:
                    try:
                        bot.load_extension(f'Commands.{folder}.{command}')
                        commands_loaded += 1
                        pcmds.append(command)
                        sys.stdout.write(f"\r[BOT.Main/CommandLoader/INFO] Commando Carregado!: {command}\n ")
                    except ExtensionAlreadyLoaded:
                            pass
                except Exception as e:
                    print(f"[{colorama.Fore.LIGHTYELLOW_EX}!!!{colorama.Fore.WHITE}] Occoreu um erro ao carregar um comando: {e}")
    

sys.stdout.write("\r[BOT.Main/CommandLoader/INFO] Carregando comandos...")
end = time.perf_counter()
sys.stdout.write(f"\r[BOT.Main/CommandLoader/Ready] Carregado {commands_loaded} Comandos em {end - started:4f} Segundos.")
print(' ')
sys.stdout.write("\r[BOT.Main/INFO] Conectando com a api...")
@bot.event
async def on_command_error(ctx,e):

    if isinstance(e,CommandNotFound):
        await ctx.reply("Desculpe esse comando não existe.")
    elif isinstance(e,TimeoutError):
        await ctx.reply("[*]Info tempo limite excedido")
    elif isinstance(e,MissingPermissions):
        await ctx.reply("Você não tem permissão para executar esse comando!")
    else:
        await ctx.reply(f"**{ctx.message.author.name}**,occoreu um erro ao executar esse comando.\nErro: `{str(e)}.`")

@bot.event
async def on_ready():

    sys.stdout.write(f"\r{colorama.Fore.GREEN}[BOT.Main/Ready] Conectado com a api BOT: {bot.user} PREFIXO: {config('PREFIX')}{ colorama.Fore.WHITE}\n")
    from Scripts.RedditController import reddit
   
    
    print(f"Conectado com a api do reddit! {reddit.update_checked}")
    await bot.change_presence(
        activity=discord.Game(name="Bot Reiniciado!"),
        status=discord.Status.online)
    time.sleep(5)
    bot.loop.create_task(change_s())
    bot.loop.create_task(run_memc())
async def run_memc():
    await InitMemCleaner()

async def change_s():

  games:list = ["Roblox", "Minecraft", "A alpha 1.2.4 do minecraft Já existiu?", "O Herobrines Já existiu?",
             "Minecraft Bedrock Edition", "Minecraft java Edition"]
  while True:
        
        selected_status = random.choice(games)
        await bot.change_presence(activity=discord.Game(name=f"Uso de ram: {round( py.memory_info()[0]  / 1000000):.2f}MB "),status=discord.Status.online)
        await asyncio.sleep(10)
        await bot.change_presence(
            activity=discord.Game(name=selected_status),
            status=discord.Status.online)
        await asyncio.sleep(10)
        await bot.change_presence(
      activity=discord.Game(name="Feito em Python!"),
      status=discord.Status.online)
        await asyncio.sleep(10)
async def on_message(message):

	# INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
	await bot.process_commands(message)


try:
    bot.run(config('TOKEN'))
except Exception as e:
    print(f"\n\nBot Desligado Motivo: {e}\n\n")