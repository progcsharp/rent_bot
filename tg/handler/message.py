from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from State.Card import Card
from State.Register import Register
from db.handler.get import get_user_by_password, get_user, get_info, get_moder, get_message
from db.handler.update import update_user_by_password, update_user_tg_id, update_user_card
from keyboards.Keyboard import personal_account


async def message_pass(message: types.Message, state: FSMContext):
    if await get_user_by_password(password=message.text):
        await state.update_data(password=message.text)
        await state.set_state(Register.name)
        await update_user_tg_id(message.text, message.from_user.id)
        await message.answer("Пароль верный введите ФИО")
        return

    await state.set_state(Register.password)
    await message.answer("Пароль не верный попробуйте еще раз")


async def message_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await update_user_by_password(data["password"], data["name"], str(data["name"]).lower())
    # await state.set_state(Card.number)

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
            text="Ввести карту",
            callback_data='card'),
        types.InlineKeyboardButton(
            text="Личный кабинет",
            callback_data='account'),
    )

    await message.answer("регистрация закончена \nхотите сейчас ввести карту?", reply_markup=builder.as_markup())


async def message_card(message: types.Message, state: FSMContext):
    await update_user_card(message.from_user.id, message.text)
    await state.clear()
    mess = await get_message("message_reg")
    await message.answer(mess, reply_markup=personal_account())


async def message_balance(message: types.Message):
    user = await get_user(message.from_user.id)
    await message.answer(f"Ваш баланс: {user.bonus}")


async def message_withdrawal(message: types.Message):
    user = await get_user(message.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
            text="Подтвердить",
            callback_data='confirmed'),
        types.InlineKeyboardButton(
            text="Изменить карту",
            callback_data='card')
    )
    await message.answer(f"Вы хотите вывести {user.bonus} бонусов на банковскую карту с номером {user.cart}", reply_markup=builder.as_markup())


async def message_payment(message: types.Message):
    user = await get_user(message.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести карту",
        callback_data='card')
    )

    await message.answer(f"Вот ваша карта {user.cart}. Хотите изменить?", reply_markup=builder.as_markup())


async def message_info(message: types.Message):
    info = await get_info()
    mess = await get_message("message_info")
    await message.answer(mess)
    await message.answer(f"{info.title}\n\n{info.article}")

