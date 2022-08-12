from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from .handlers import dp

from ..storage import ErrSt
from ..keyboards import start_keyboard, send
from ..utils import get_random_instance, get_all_vars
from ..models import session, Alg
from ..manage_mail.send_mail import send_mail_err



# Обработка команды '/start'
@dp.message_handler(commands=['start'])
async def process_start(message: types.Message):
    text_msg = f'Привет, <i><b>{message.from_user.full_name}</b></i> я бот, который может помочь в изучении алгоритмов и структур данных. Вводи или выбирай ниже интересующую тебя тему и приступай к изучению!:)'
    await message.reply(text_msg, reply_markup=start_keyboard)


# Обработка команды '/random_alg' - случайный алгоритм
@dp.message_handler(commands=['random_alg'])
async def process_random_alg(message: types.Message):
    text_msg, markup = get_random_instance(alg=True)
    await message.reply(text_msg, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)


# Обработка команды '/random_struct' - случайная структура
@dp.message_handler(commands=['random_struct'])
async def process_random_struct(message: types.Message):
    text_msg, markup = get_random_instance(alg=False)
    await message.reply(text_msg, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)


# Обработка команды '/all' - все доступные структуры и алгоритмы
@dp.message_handler(commands=['all'])
async def process_all(message: types.Message):
    text_msg, markup = get_all_vars(all=True)
    await message.reply(text_msg, reply_markup=markup)


# Обработка команды '/all_algs' - все доступные алгоритмы
@dp.message_handler(commands=['all_algs'])
async def process_all_algs(message: types.Message):
    text_msg, markup = get_all_vars(algs=True)
    await message.reply(text_msg, reply_markup=markup)


# Обработка команды '/all_structs' - все доступные структуры данных
@dp.message_handler(commands=['all_structs'])
async def process_all_structs(message: types.Message):
    text_msg, markup = get_all_vars(structs=True)
    await message.reply(text_msg, reply_markup=markup)


# Обработка отправки сообщения на почту
@dp.message_handler(Text(equals=[send.text]), state=ErrSt.err_alg_name)
async def process_send_mail(message: types.Message, state: FSMContext):
    data = await state.get_data()
    err_text = data['err_alg_name'] # Текст (алгоритм/структура), который привёл к ошибке 'ненахода'

    text_msg, markup = send_mail_err(err_text)
    await message.reply(text_msg, reply_markup=markup)
    await state.finish()