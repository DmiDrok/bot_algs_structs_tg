from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from sqlalchemy import func

from .commands import dp

from ..models import session, Alg
from ..utils import get_instance, get_file_by_id
from ..keyboards import email_keyboard, file_keyboard, file_btn
from ..storage import AlgSt, ErrSt

import asyncio


# Получение файла с реализацией алгоритма/структуры данных
@dp.message_handler(Text(equals=file_btn.text), state=AlgSt.alg_name)
async def process_get_file(message: types.Message, state: FSMContext):
    await message.answer('Отсылаю файл.')
    data = await state.get_data()
    file_id = data['alg_id']
    file = get_file_by_id(file_id)
    await dp.bot.send_document(message.chat.id, document=file)
    
    await state.finish()

# Обработка callback-ов, которые не прошли проверки сверху
@dp.callback_query_handler(state='*')
async def process_all_algs_structs(callback: types.CallbackQuery, state: FSMContext):
    text_msg, markup = get_instance(callback.data)
    await callback.message.answer(text_msg, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)
    
    await AlgSt.alg_name.set()
    await state.update_data(alg_id=callback.data)

# Обработка сообщений, не прошедших проверки сверху
@dp.message_handler(state='*')
async def process_instance(message: types.Message, state: FSMContext):
    user_text = message.text.lower().split()
    if len(user_text) <= 35:
        for word in user_text:
            data_db = session.query(Alg).filter(func.lower(Alg.title).contains(word)).first()
    
    text_msg, markup = get_instance(data_db)

    await message.reply(text_msg, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)

    if not data_db:
        await ErrSt.err_alg_name.set()
        await state.update_data(err_alg_name=message.text)
    else:
        await AlgSt.alg_name.set()
        await state.update_data(alg_id=data_db.data_id)