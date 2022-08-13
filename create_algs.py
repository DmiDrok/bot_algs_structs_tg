from mybot import session
from mybot.models import Alg

import os


def create_all():
    """
        Данная функция создаёт файлы внутри папки со всеми алгоритмами/структурами
        Внутри файлов будет содержаться код, указанный в поле .code нашей таблицы (Alg)
    """

    all_algs = session.query(Alg).all()
    for alg in all_algs:
        with open(os.path.join('all_algs', f'{alg.data_id}.py'), 'w') as file:
            file.write(alg.code)
