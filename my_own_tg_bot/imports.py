from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot_token import API_TOKEN


storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
