import gc,colorama,time,os,psutil,asyncio
from Scripts.getramusage import getrusage
pid = os.getpid()
async def Initgc():
    gc.enable()
    print(f'[{colorama.Fore.GREEN}*{colorama.Fore.RESET}] Garbage collector Started.')
    await garcf()
async def garcf():
    while True:
        memoryUse = getrusage()
        if memoryUse >= 60:
            print(f'[{colorama.Fore.LIGHTYELLOW_EX}!!!{colorama.Fore.RESET}] Garbage collector {memoryUse} > 60')
            await asyncio.sleep(60)
        else:
            await asyncio.sleep(300)
            print(f'[{colorama.Fore.GREEN}*{colorama.Fore.RESET}] Init Garbage collect')    
            gc.collect()
            

    