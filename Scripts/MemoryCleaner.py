import gc,colorama,time,os,psutil,asyncio

pid = os.getpid()
py = psutil.Process(pid)
async def InitMemCleaner():
    
    print(f'[{colorama.Fore.GREEN}*{colorama.Fore.RESET}] Memory Cleaner Started.')
    await MemCleaner()
async def MemCleaner():
    while True:
        memoryUse = round( py.memory_info()[0]  / 1000000)
        if memoryUse >= 60:
            print(f'[{colorama.Fore.LIGHTYELLOW_EX}!!!{colorama.Fore.RESET}] MEMORY USAGE IS HIGH CLEANING RAM... ')
            await asyncio.sleep(60)
        else:
            await asyncio.sleep(300)
            print(f'[{colorama.Fore.GREEN}*{colorama.Fore.RESET}] Cleaning RAM....')    
            gc.collect()
        

    