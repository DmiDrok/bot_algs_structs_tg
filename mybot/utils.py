from aiogram import md

from .keyboards import randoms_keyboard, email_keyboard
from .models import Alg, session

import random
import emoji
import os


def get_random_instance(alg=True):
    """
        Функция получения случайного алгоритма (если alg is True)
        И иначе - функция получения случайной структуры данных.
        Возвращает первым аргументом текст сообщения,
        Вторым - клавиатуру к нему
    """
    which_type = 1 if alg else 2
    top_bound = session.query(Alg).filter_by(type=which_type).count()
    data_db = session.query(Alg).filter_by(type=which_type)[random.randint(0, top_bound-1)] # Выбираем случайный из БД
    
    markup = None
    if data_db:
        text_msg = f'{data_db.title}\n\n{data_db.description}\n\nРеализация на языке программирования {emoji.emojize(":snake:")} Python:`\n{md.quote_html(data_db.code)}`'
        markup = randoms_keyboard
    else:
        text_msg = 'Что-то пошло не по плану, попробуйте позже...'

    return text_msg, markup


def get_all_vars(all=False, algs=False, structs=False):
    """
        Функция которая вернёт строку со всеми алгоритмами и структурами.
        Второй аргумент - клавиатура.
    """
    if all:
        text_msg = '<b>Все доступные алгоритмы и структуры данных:</b>\n'
    elif algs:
        text_msg = '<b>Все доступные алгоритмы:</b>\n'
    elif structs:
        text_msg = '<b>Все доступные структуры данных:</b>\n'

    markup = randoms_keyboard
    if all or algs:
        algs = session.query(Alg).filter_by(type=1).all()
        text_msg += '\n<b>Алгоритмы:</b>\n'
        for i, alg in enumerate(algs, start=1):
            text_msg += f'{i}. {alg.title}\n'
    
    if all or structs:
        structs = session.query(Alg).filter_by(type=2).all()
        text_msg += '\n<b>Структуры данных:</b>\n'
        for i, struct in enumerate(structs, start=1):
            text_msg += f'{i}. {struct.title}\n'


    return text_msg, markup

def get_all_algs():
    """
        Функция которая вернёт строку со всеми алгоритмами. Второй аргумент - клавиатура.
    """
    markup = randoms_keyboard
    text_msg = '<b>Все доступные алгоритмы:</b>\n'
    algs = session.query(Alg).filter_by(type=1).all()

    for i, alg in enumerate(algs, start=1):
        text_msg += f'{i}. {alg.title}\n'

    return text_msg, markup

def get_instance(data):
    """
        Функция получения записи из БД по полю data_id
    """

    markup = None
    data_db = None
    file = None
    if data: # Если выборка существует - делаем сообщение на её основе
        if type(data) is Alg:
            data_db = session.query(Alg).filter_by(data_id=data.id).first()
        else: # Если передан был callback от кнопки (сразу id)
            data_db = session.query(Alg).filter_by(data_id=data).first()

        code = data_db.code

        text_msg = f'{data_db.title}\n\n{data_db.description}\n\nРеализация на языке программирования {emoji.emojize(":snake:")} Python:\n`{code}`'
        markup = randoms_keyboard
        file = open(os.path.join('all_algs', f'{data_db.data_id}.py'), 'rb')
    elif not data_db: # Если выборки не существует - уведомляем об отсутствии
        text_msg = f'Прошу прощения, но я пока не обладаю знаниями по этой теме.'
        markup = email_keyboard

    print(f'ЭТО ФАЙЛ: {file}')
    return text_msg, markup, file
