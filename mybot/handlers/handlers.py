from aiogram import types
from aiogram.dispatcher import FSMContext

from ..bot_dp import dp
from ..keyboards import algs_keyboard, structs_keyboard
from ..utils import get_random_instance, get_instance
from ..storage import AlgSt

import asyncio


# Обработчик при выборе 'Алгоритмы'
@dp.callback_query_handler(lambda msg: msg.data == 'algs', state='*')
async def process_algs(callback: types.CallbackQuery):
    text_msg = f'Хорошо, ты выбрал <i><b>"Алгоритмы"</b></i>!\n\nВводи название любого алгоритма - я с подробностями постараюсь описать его.'
    await callback.message.reply(text_msg)
    await asyncio.sleep(1/2)
    text_msg = f'К слову, вот некоторые из алгоритмов, которые я знаю:'
    await callback.message.reply(text_msg, reply_markup=algs_keyboard)


# Обработчик при выборе 'Структуры данных'
@dp.callback_query_handler(lambda msg: msg.data == 'structs', state='*')
async def process_structs(callback: types.CallbackQuery):
    text_msg = 'Хорошо, ты выбрал <i><b>"Структуры данных"</b></i>!\n\nВводи название любой структуры - я с подробностями постараюсь описать её.'
    await callback.message.reply(text_msg)
    await asyncio.sleep(1/2)
    text_msg = f'К слову, вот некоторые из структур, которые я знаю:'
    await callback.message.reply(text_msg, reply_markup=structs_keyboard)


# Обработчик при выборе 'Случайный алгоритм'
@dp.callback_query_handler(lambda msg: msg.data == 'random_alg', state='*')
async def process_random_alg(callback: types.CallbackQuery, state: FSMContext):
    text_msg, markup, instance = get_random_instance(alg=True)
    await callback.message.answer(text_msg, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)

    await AlgSt.alg_name.set()
    await state.update_data(alg_id=instance.data_id)


# Обработчик при выборе 'Случайная структура'
@dp.callback_query_handler(lambda msg: msg.data == 'random_struct', state='*')
async def process_random_struct(callback: types.CallbackQuery, state: FSMContext):
    text_msg, markup, instance = get_random_instance(alg=False)
    await callback.message.answer(text_msg, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)

    await AlgSt.alg_name.set()
    await state.update_data(alg_id=instance.data_id)
