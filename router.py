import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile, CallbackQuery

from config import bot
from src.keyboard import menu_keyboard_maker, menu_slovar, faq_keyboard_maker, faq_answers, courses_keyboard_maker, \
    hello_button, hello_slovar, gender_keyboard_maker, yesorno_keyboard_maker, yesorno_slovar, main_test_keyboard_maker
from src.states import UserStates

user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await bot.send_animation(
        chat_id=message.chat.id,
        animation="CgACAgIAAxkBAAIBT2k0J8xAUhpqB5FQPnHxUvOuSsGtAAJwiwAC5R2hSe9b7bYk1cVlNgQ",
        caption="""Привет 👋
Я антистресс-бот помощник Зови. 
Меня придумала команда квалифицированных психологов для помощи тем, кто очень устал и переживает сильный стресс.""",
    )
    await asyncio.sleep(1)
    await bot.send_message(
        chat_id=message.chat.id,
        text="""Общаясь со мной, вы можете:
        🟠пройти психологическое тестирование
        🟠узнать пошаговые рекомендации для самопомощи
        🟠пройти обучающие курсы 
        🟠получить контакты квалифицированных психологов и психологических центров

Я очень хочу помочь вам! 🫂 Чтобы поскорее к этому приступить, давайте немного познакомимся. 
        
Для общение со мной используйте кнопки внизу экрана вашего устройства:
        """,
        reply_markup=hello_button()
    )
    await state.set_state(UserStates.hello)


@user_router.message(UserStates.hello, F.text == hello_slovar["hello"])
async def hello(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text="""Расскажите немного о себе""",
        reply_markup=ReplyKeyboardRemove()
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text="""Кто вы?
Используйте кнопки внизу сообщения для выбора ответа:""",
        reply_markup=gender_keyboard_maker()
    )
    await state.set_state(UserStates.gender)


@user_router.callback_query(UserStates.gender, F.data.in_(hello_slovar.keys()))
async def gender(callback_query: CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=None
    )
    if callback_query.data == "female":
        await bot.send_message(
            chat_id=callback_query.from_user.id,
            text="""Знаете, я заметил одну вещь 🤔 женщины в разном возрасте переживают стресс совсем по-разному.
Поэтому мне очень важно знать — на каком вы сейчас жизненном этапе?

Напишите в сообщении сколько вам лет:""",
        )
    else:
        await bot.send_message(
            chat_id=callback_query.from_user.id,
            text="""Мужчины редко признаются, что им тяжело, поэтому то, что ты здесь — уже большой шаг.
Поэтому мне очень важно знать — в каком вы сейчас жизненном этапе? 

Напишите в сообщении сколько вам лет:""",
        )
    await state.set_state(UserStates.age)


@user_router.message(UserStates.age, F.text.isdigit())
async def age(message: Message, state: FSMContext):
    if int(message.text) < 18:
        await bot.send_message(
            chat_id=message.chat.id,
            text="""Вам должно быть 18 лет или больше. Попробуйте ещё раз:""")
        return
    elif int(message.text) > 100:
        await bot.send_message(
            chat_id=message.chat.id,
            text="""Вам должно быть меньше 100 лет. Попробуйте ещё раз:""")
        return
    await bot.send_message(
        chat_id=message.chat.id,
        text="""Ещё один маленький, но важный вопрос…
        
Сейчас многие живут с тяжёлым чувством, когда близкий человек на передовой.
И знаю, как сильно это влияет на сон, нервы, силы…

Можешь не рассказывать подробностей — просто скажи, есть ли у тебя сейчас такой человек среди родных или самых близких?""",
        reply_markup=yesorno_keyboard_maker()
    )
    await state.set_state(UserStates.swo_family)


@user_router.message(UserStates.age)
async def age_error(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text="""Не понял. Напишите цифрами в сообщении сколько вам лет, например, 23.""",
    )
    await state.set_state(UserStates.age)


@user_router.message(UserStates.swo_family, F.text.in_(yesorno_slovar.values()))
async def swo_family(message: Message, state: FSMContext):
    await bot.send_message(
            chat_id=message.chat.id,
            text="""Крепко обнимаю ❤️‍🩹
Внизу кнопки — тут ты можешь пройти психологический тест, задать мне любой вопрос, получить техники или найти специалиста.
Выбирай, что нужно прямо сейчас:""",
            reply_markup=menu_keyboard_maker()
        )
    await state.set_state(UserStates.menu)


@user_router.message(UserStates.menu, F.text == menu_slovar["buttonkey3"])
async def faq(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text=("Часто задаваемые вопросы ❤️\n\n"
        "Тыкайте на любой вопрос ниже — я сразу подробно отвечу.\n"),
        reply_markup=faq_keyboard_maker()
    )


@user_router.callback_query(UserStates.menu, F.data.in_(faq_answers.keys()))
async def answers(callback_query: CallbackQuery, state: FSMContext):
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=faq_answers[callback_query.data]
    )


@user_router.message(UserStates.menu, F.text == menu_slovar["buttonkey2"])
async def courses(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text=("Мини-курсы, которые реально помогают ❤️\n\n"
        "Каждый курс — это 5–12 коротких уроков по 3–10 минут.\n"
        "Можно проходить в любом порядке и в любое время.\n"
        "Сейчас действуют специальные цены для тех, кто с нами с самого начала:"),
        reply_markup=courses_keyboard_maker()
    )


@user_router.message(UserStates.menu, F.text == menu_slovar["buttonkey1"])
async def test(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text=("""Благодаря опросу я смогу понять, как вы чувствуете себя и насколько силен ваш стресс.
После его прохождения вас ожидает:
-психологическое заключение, основанное на результатах
-рекомендации для самопомощи, к выполнению которых вы можете приступить уже сегодня
 ❤️\n\n"""),
        reply_markup=main_test_keyboard_maker()
            )
