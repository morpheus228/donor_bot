import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
# from middlewares.user_availability import UserAvailabilityMiddleware
from sqlalchemy.orm import Session

from config import Config

from handlers.account import router as account_router

# from repositories import mysql, Repository
# from services import Service


logging.basicConfig(level=logging.INFO)


def register_routers(dp: Dispatcher):
    dp.include_router(account_router)


def register_middlewares(dp: Dispatcher):
    # dp.update.outer_middleware(UserAvailabilityMiddleware(dp['repository']))
    pass


async def register_default_commands(dp: Dispatcher):
    command_list = []
    for key in dp['commands']:
        command_list.append(BotCommand(command=key[1:], description=dp['commands'][key]))

    await dp['bot'].set_my_commands(command_list)


async def main():
    Config.set()
    bot = Bot(Config.bot.token, parse_mode='HTML')

    # engine = mysql.get_engine(config.mysql)
    # repository = Repository(engine, config)
    # service = Service(repository, config)

    dp = Dispatcher(storage=MemoryStorage())
    
    dp['dp'] = dp
    dp['bot'] = bot
    # dp['service'] = service
    # dp['repository'] = repository

    dp['commands'] = {"/menu": "Меню"}

    await register_default_commands(dp)
    
    register_routers(dp)
    register_middlewares(dp)

    await dp.start_polling(dp['bot'])


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("ебать!")
