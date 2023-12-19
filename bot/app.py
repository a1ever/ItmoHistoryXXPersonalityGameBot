import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from bot.commands import register_user_commands
from storage.db import create_pool, get_session_maker, proceed_schemas, BaseModel


async def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    bot = Bot(token=os.getenv('bot_token'))

    register_user_commands(dp)

    url = "mysql+aiomysql://root:2Ghgb6fhBDBA5DaA2hhh-gBe233B-dA-@viaduct.proxy.rlwy.net:15123/railway"

    async_engine = create_pool(url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot, session_maker=session_maker)


def application(environ, start_response):
    start_response('200 ОК', [('Content-type', 'text/plain')])
    asyncio.run(main())