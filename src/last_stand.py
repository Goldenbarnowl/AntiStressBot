from aiogram import Router

last_stand_router = Router()


@last_stand_router.message()
async def echo(message):
    await message.answer("Я вас не понимаю")
    print(message)

