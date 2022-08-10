from aiogram import executor, types
from mybot import bot, dp

from config import ADMIN_ID


# Функция отправки письма администратору при запуске
async def send_start(message):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Начать работу с ботом'),
        types.BotCommand('help', 'Помощь по командам бота.'),
        types.BotCommand('random_alg', 'Случайный алгоритм'),
        types.BotCommand('random_struct', 'Случайная структура данных'),
    ])
    await bot.send_message(ADMIN_ID, 'Бот запущен.')


# Точка входа
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=send_start)

