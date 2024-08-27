from aiogram.fsm.state import StatesGroup, State


class Card(StatesGroup):
    number = State()
