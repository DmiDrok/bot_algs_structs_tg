from aiogram import types

from .handlers import dp
from .keyboards import start_keyboard
from .utils import get_random_instance 


# Обработка команды '/start'
@dp.message_handler(commands=['start'])
async def process_start(message: types.Message):
    text_msg = f'Привет, <i><b>{message.from_user.full_name}</b></i> я бот, который может помочь в изучении алгоритмов и структур данных. Вводи или выбирай ниже интересующую тебя тему и приступай к изучению!:)'
    await message.reply(text_msg, reply_markup=start_keyboard)


# Обработка команды '/random_alg' - случайный алгоритм
@dp.message_handler(commands=['random_alg'])
async def process_random_alg(message: types.Message):
    text_msg, markup = get_random_instance(alg=True)
    await message.reply(text_msg, reply_markup=markup)


# Обработка команды '/random_struct' - случайная структура
@dp.message_handler(commands=['random_struct'])
async def process_random_struct(message: types.Message):
    text_msg, markup = get_random_instance(alg=False)
    await message.reply(text_msg, reply_markup=markup)
    