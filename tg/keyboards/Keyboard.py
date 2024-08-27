from aiogram import types


def personal_account():
    kb = [
        [types.KeyboardButton(text="Баланс"), types.KeyboardButton(text="Вывод бонусов")],
        [types.KeyboardButton(text="Способ оплаты"), types.KeyboardButton(text="Информация")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    return keyboard
