from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from State.Register import Register
from db.handler.get import get_user_by_tg_id
from keyboards.Keyboard import personal_account


async def cmd_start(message: types.Message, state: FSMContext):

    if await get_user_by_tg_id(message.from_user.id):
        await state.set_state(Register.password)
        await message.answer("Здравствуйте! Вы не зарегестрированны введите пароль")
        return

    await message.answer('Личный кабинет', reply_markup=personal_account())
