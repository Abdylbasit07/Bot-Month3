from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
ADMINS= [5322416459,]
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
