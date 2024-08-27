from aiogram import Dispatcher, F

from handler.callback import call_card, call_account, call_confirmed


async def register_handlers_callback(dp: Dispatcher):
    dp.callback_query.register(call_card, F.data == 'card')
    dp.callback_query.register(call_account, F.data == 'account')
    dp.callback_query.register(call_confirmed, F.data == 'confirmed')
