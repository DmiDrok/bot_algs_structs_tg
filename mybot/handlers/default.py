from aiogram import types
from sqlalchemy import func

from .commands import dp

from ..storage import storage_errors
from ..models import session, Alg
from ..utils import get_instance
from ..keyboards import email_keyboard

import asyncio


# Обработка callback-ов, которые не прошли проверки сверху
@dp.callback_query_handler()
async def process_all_algs_structs(callback: types.CallbackQuery):
    text_msg, markup, file = get_instance(callback.data)
    await callback.message.answer(text_msg, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)
    
    await asyncio.sleep(1/2)

    if file:
        await callback.message.answer('Прикрепляю файл с реализацией:') 
        await dp.bot.send_document(callback.message.chat.id, file)
    
    print(file)
    print('----------')

# Обработка сообщений, не прошедших проверки сверху
@dp.message_handler()
async def process_instance(message: types.Message):
    user_text = message.text.lower().split()
    if len(user_text) <= 35:
        for word in user_text:
            data_db = session.query(Alg).filter(func.lower(Alg.title).contains(word)).first()
    
    text_msg, markup, file = get_instance(data_db)
    if markup is email_keyboard: # Если клавиатура специально для отправки сообщения об ошибке - в хранилище ошибок добавляем то, что её вызвало
        storage_errors[message.from_user.id] = message.text

    await message.reply(text_msg, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)

    if file:
        await dp.bot.send_document(message.chat.id, file)