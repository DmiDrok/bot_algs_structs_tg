from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from config import API_TOKEN


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
