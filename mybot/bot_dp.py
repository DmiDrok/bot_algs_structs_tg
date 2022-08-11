from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from config import API_TOKEN


bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
