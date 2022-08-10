from .keyboards import randoms_keyboard
from .models import Alg, session

import random
import emoji

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
        text_msg = f'<b>{data_db.title}</b>\n\n{data_db.description}\n\n<b>Реализация на языке программирования {emoji.emojize(":snake:")} Python:</b>\n<code><pre>{data_db.code}</pre></code>'
        markup = randoms_keyboard
    else:
        text_msg = 'Что-то пошло не по плану, попробуйте позже...'

    return text_msg, markup
