from ..keyboards import randoms_keyboard
from config import ADMIN_EMAIL, SECRET_KEY_EMAIL

from email.mime.text import MIMEText

import smtplib


def send_mail_err(text):
    """
        Сообщение отправки сообщения на почту о
        не найденном алгоритме / структуре данных.
        Возвращает первым аргументом текст,
        Вторым - клавиатуру.
    """
    
    text_msg = 'Сообщение успешно отправлено. Мы проверим алгоритм/структуру и постараемся добавить в бота как можно скорее.\n\n<b><u>Спасибо :3</u></b>'
    markup = randoms_keyboard

    # Логика отправки письма
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(ADMIN_EMAIL, SECRET_KEY_EMAIL)

    msg = MIMEText(f'<h3>Был не найден следующий экземпляр: <br> "<u>{text}</u>"</h3>', 'html')
    msg['From'] = 'Телеграм-Бот (Алгоритмы и структуры данных)'
    msg['Subject'] = 'Сообщение об ошибке ненахода в телеграм-боте.'

    server.sendmail(ADMIN_EMAIL, ADMIN_EMAIL, msg.as_string()) # Отправляем сообщение


    return text_msg, markup