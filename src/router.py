from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile, CallbackQuery

from config import bot
from src.keyboard import menu_keyboard_maker, menu_slovar, faq_keyboard_maker, faq_answers
from src.states import UserStates

user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Привет! 👋 (место для приветсвия)",
        reply_markup=menu_keyboard_maker(),
    )
    await state.set_state(UserStates.menu)

@user_router.message(UserStates.menu, F.text == menu_slovar["buttonkey3"])
async def faq(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Вот тебе faq",
        reply_markup=faq_keyboard_maker()
    )

@user_router.callback_query(UserStates.menu)
async def answers(callback_query: CallbackQuery, state: FSMContext):
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=faq_answers[callback_query.data]
    )