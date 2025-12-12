import asyncio
import logging
import sys

from aiogram.methods import DeleteWebhook

from config import dp, bot
from src.courses_directory.course_one import course_one_router
from src.courses_directory.course_two import course_two_router
from src.last_stand import last_stand_router
from src.router import user_router
from src.router_tests.main_test_router import test_router


async def start():
    dp.include_router(user_router)
    user_router.include_routers(course_one_router)
    dp.include_router(test_router)
    dp.include_router(last_stand_router)
    try:
        await bot(DeleteWebhook(drop_pending_updates=True))
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())
