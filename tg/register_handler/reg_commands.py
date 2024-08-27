from aiogram import Dispatcher
from aiogram.filters import Command

from handler.commands import cmd_start


async def register_handlers_commands(dp: Dispatcher):
    dp.message.register(cmd_start, Command('start'))

