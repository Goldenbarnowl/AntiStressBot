from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, URLInputFile

from config import bot
from src.states import UserStates

course_one_router = Router()

@course_one_router.callback_query(UserStates.menu, F.data == "course1")
async def answers(callback_query: CallbackQuery, state: FSMContext):
    await bot.send_photo(
        chat_id=callback_query.from_user.id,
        caption="text",
        photo=URLInputFile("https://trainingtechnology.ru/wp-content/uploads/2024/01/trening-emoczionalnyj-intellekt.jpg")
    )