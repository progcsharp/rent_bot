from aiogram import types
from aiogram.fsm.context import FSMContext

from db.handler.get import get_message, get_moder, get_user
from keyboards.Keyboard import personal_account
from State.Card import Card
# from utils import message_moder
from config import bot


async def call_card(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card.number)
    await callback.message.answer("Введите номер карты")
    # builder = InlineKeyboardBuilder()
    # builder.add(types.InlineKeyboardButton(
    #     text="Купить ключь",
    #     callback_data='buy_key'),
    #     types.InlineKeyboardButton(
    #     text="Мои клучи",
    #     callback_data='my_keys')
    # )
    #
    # await callback.message.answer('вы вошли в личный кабинет чтобы посмотреть инструкцию по использованию введите /help',
    #                               reply_markup=builder.as_markup())

#
# async def call_buy(callback: types.CallbackQuery):
#     await callback.message.answer('Здесь будет продажа')
#
#
# async def call_my_keys(callback: types.CallbackQuery):
#     await callback.message.answer('Здесь будут ваши ключи')


async def call_account(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    message = await get_message("message_reg")
    await callback.message.answer(message, reply_markup=personal_account())


async def call_confirmed(callback: types.CallbackQuery):
    message = await get_message("message_bonus")
    # await message_moder(callback.from_user.id)
    user = await get_user(callback.from_user.id)
    moder = await get_moder()
    await bot.send_message(int(moder), f"Заявка на вывод бонусов:\nФИО:{user.name}\nКарта:{user.cart}\nБонусы:{user.bonus}")
    await callback.message.answer(message)
