from aiogram import executor, types

from mybot import bot, dp

from create_algs import create_all

from config import ADMIN_ID

# Функция отправки письма администратору при запуске
async def send_start(message):
    create_all() # Создаём все алгоритмы / структуры в папке с ними
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Начать работу с ботом'),
        types.BotCommand('all', 'Все алгоритмы и структуры, которые знает бот.'),
        types.BotCommand('all_algs', 'Все алгоритмы, которые знает бот.'),
        types.BotCommand('all_structs', 'Все структуры данных, которые знает бот.'),
        types.BotCommand('random_alg', 'Случайный алгоритм'),
        types.BotCommand('random_struct', 'Случайная структура данных'),
    ])
    await bot.send_message(ADMIN_ID, 'Бот запущен.')


# Точка входа
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=send_start)

