from aiogram.types import BotCommand


async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота!"),
        BotCommand(command="/help", description="Как это работает?"),
        BotCommand(command="/manu", description="Вернуться к меню!")
    ]
    await bot.set_my_commands(commands)
