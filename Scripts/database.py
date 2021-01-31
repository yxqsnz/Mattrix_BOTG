from discord import client
from pymongo import MongoClient
from Scripts.envcontroller import ReturnEnv
client = MongoClient(ReturnEnv('db'))
db = client.get_database("BOT")
Economy = db.Economy
