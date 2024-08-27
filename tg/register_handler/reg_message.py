from aiogram import Dispatcher, F

from State.Card import Card
from State.Register import Register
from handler.message import message_pass, message_name, message_card, message_balance, \
    message_withdrawal, message_info, message_payment


async def register_handlers_message(dp: Dispatcher):
    dp.message.register(message_pass, Register.password)
    dp.message.register(message_name, Register.name)
    dp.message.register(message_card, Card.number)
    dp.message.register(message_balance, F.text == "Баланс")
    dp.message.register(message_withdrawal, F.text == "Вывод бонусов")
    dp.message.register(message_payment, F.text == "Способ оплаты")
    dp.message.register(message_info, F.text == "Информация")
