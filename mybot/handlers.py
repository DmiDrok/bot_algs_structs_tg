from aiogram import types

from .bot_dp import dp
from .keyboards import start_keyboard, algs_keyboard, structs_keyboard
from .keyboards import randoms_keyboard
from .models import Alg, session
from .utils import get_random_instance

import asyncio
import emoji
import random


# Обработчик при выборе 'Алгоритмы'
@dp.callback_query_handler(lambda msg: msg.data == 'algs')
async def process_algs(callback: types.CallbackQuery):
    text_msg = f'Хорошо, ты выбрал <i><b>"Алгоритмы"</b></i>!\n\nВводи название любого алгоритма - я с подробностями постараюсь описать его.'
    await callback.message.reply(text_msg)
    await asyncio.sleep(1/2)
    text_msg = f'К слову, вот некоторые из алгоритмов, которые я знаю:'
    await callback.message.reply(text_msg, reply_markup=algs_keyboard)


# Обработчик при выборе 'Структуры данных'
@dp.callback_query_handler(lambda msg: msg.data == 'structs')
async def process_structs(callback: types.CallbackQuery):
    text_msg = 'Хорошо, ты выбрал <i><b>"Структуры данных"</b></i>!\n\nВводи название любой структуры - я с подробностями постараюсь описать её.'
    await callback.message.reply(text_msg)
    await asyncio.sleep(1/2)
    text_msg = f'К слову, вот некоторые из структур, которые я знаю:'
    await callback.message.reply(text_msg, reply_markup=structs_keyboard)


# Обработчик при выборе 'Случайный алгоритм'
@dp.callback_query_handler(lambda msg: msg.data == 'random_alg')
async def process_random_alg(callback: types.CallbackQuery):
    text_msg, markup = get_random_instance(alg=True)
    await callback.message.reply(text_msg, reply_markup=markup)


# Обработчик при выборе 'Случайная структура'
@dp.callback_query_handler(lambda msg: msg.data == 'random_struct')
async def process_random_struct(callback: types.CallbackQuery):
    text_msg, markup = get_random_instance(alg=False)
    await callback.message.reply(text_msg, reply_markup=markup)


# Обработка callback-ов, которые не прошли проверки сверху
@dp.callback_query_handler()
async def process_all_algs_structs(callback: types.CallbackQuery):
    data_db = session.query(Alg).filter_by(data_id=callback.data).first()

    markup = None
    if data_db: # Если выборка существует - делаем сообщение на её основе
        code = data_db.code
        
        text_msg = f'<b>{data_db.title}</b>\n\n{data_db.description}\n\n<b>Реализация на языке программирования {emoji.emojize(":snake:")} Python:</b>\n<code>{code}</code>'
        markup = randoms_keyboard
    else: # Если выборки не существует - уведомляем об отсутствии
        text_msg = f'<b>Прошу прощения</b>, но я пока не обладаю знаниями по этой теме.'

    await callback.message.answer(text_msg, reply_markup=markup)