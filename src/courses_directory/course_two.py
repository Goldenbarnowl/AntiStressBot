from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, URLInputFile, LabeledPrice, PreCheckoutQuery, Message

from config import bot
from src.states import UserStates

course_two_router = Router()

@course_two_router.callback_query(UserStates.menu, F.data == "course2")
async def answers(callback_query: CallbackQuery, state: FSMContext):

    invoice_message = await bot.send_invoice(
        chat_id=callback_query.from_user.id,
        title='Когнитивно поведенческий курс',
        description=f'Курс проводится с 30.11.25 по 30.01.26',
        payload="2",
        provider_token="1744374395:TEST:e5d71d19d5c4ad74014a",
        photo_url='https://trainingtechnology.ru/wp-content/uploads/2024/01/trening-emoczionalnyj-intellekt.jpg',
        currency='rub',
        prices=[LabeledPrice(label='Курс', amount=600000)],
        start_parameter='Pay',
        need_name=True,
        need_phone_number=True,
        protect_content=True,
        request_timeout=60,
    )
@course_two_router.pre_checkout_query(UserStates.menu)
async def pre_checkout(query: PreCheckoutQuery, state: FSMContext):
    """
    Функция обрабатывает проверку оплаты
    """
    await bot.answer_pre_checkout_query(query.id, ok=True)


@course_two_router.message(F.successful_payment)
async def shipping(message: Message, state: FSMContext):

        await bot.send_message(
            chat_id=message.chat.id,
            text="Спасибо за оплату, вы успешно купили курс"
        )