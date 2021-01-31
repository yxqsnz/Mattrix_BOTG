from dotenv import load_dotenv
import os
def ReturnEnv(v):
    load_dotenv('config.env')
    return os.getenv(v)