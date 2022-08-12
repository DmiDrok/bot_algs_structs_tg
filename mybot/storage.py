from aiogram.dispatcher.filters.state import StatesGroup, State


class ErrSt(StatesGroup):
    err_alg_name = State()

class AlgSt(StatesGroup):
    alg_name = State()