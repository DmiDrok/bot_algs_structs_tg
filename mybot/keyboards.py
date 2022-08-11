from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура при старте
start_keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Алгоритмы', callback_data='algs')).add(InlineKeyboardButton(text='Структуры данных', callback_data='structs'))


# Клавиатруа при выборе алгоритмов
text_data = (
    ['Сортировка пузырьком', 'bubble_sort'],
    ['Алгоритм Евклида', 'euclidean'],
    ['Факториал', 'factorial']
)
algs_keyboard = InlineKeyboardMarkup(row_width=1)
for text, data in text_data:
    algs_keyboard.add(InlineKeyboardButton(text, callback_data=data))


# Клавиатура при выборе структур данных
text_data = (
    [f'Бинарное дерево', 'binary_tree'],
    ['Связный список', 'linked_list'],
    ['Очередь', 'queue'],
)
structs_keyboard = InlineKeyboardMarkup(row_width=1)
for text, data in text_data:
    structs_keyboard.add(InlineKeyboardButton(text, callback_data=data))


# Клавиатура для случайного алгоритма/структуры
randoms_keyboard = InlineKeyboardMarkup()
btn_random_alg = InlineKeyboardButton('Случайный алгоритм', callback_data='random_alg')
btn_random_struct = InlineKeyboardButton('Случайная структура', callback_data='random_struct')
randoms_keyboard.add(btn_random_alg, btn_random_struct)

# Клавиатура для отправки письма на почту
email_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
send = KeyboardButton('Отправить письмо об ошибке на почту.')
email_keyboard.add(send)