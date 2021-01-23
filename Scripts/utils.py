import os
import subprocess
from multiprocessing import TimeoutError
from multiprocessing.pool import ThreadPool
def timeout(seconds):
    def decorator(function):
        def wrapper(*args, **kwargs):
            pool = ThreadPool(processes=1)
            result = pool.apply_async(function, args=args, kwds=kwargs)
            try:
                return result.get(timeout=seconds)
            except TimeoutError as e:
                return e
        return wrapper
    return decorator


@timeout(8)
def capturecmdexit(code):
    return  subprocess.check_output([code],shell=True,stdin=None).decode('utf-8')
@timeout(8)
def runJSScript(scriptname:str):
           
           return 