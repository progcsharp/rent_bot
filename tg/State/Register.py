from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    password = State()
    name = State()

