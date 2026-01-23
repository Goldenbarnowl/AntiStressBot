from aiogram.types import KeyboardButton, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


hello_slovar = {"hello": "Я согласен на обработку персональных данных 👋", "female": "👩 Женщина‍", "male": "👨 Мужчина"}
yesorno_slovar = {"yes": "Да", "no": "Нет"}
menu_slovar = {"buttonkey1": "👁 Тестирование", "buttonkey2": "💡 Курсы", "buttonkey3": "❓ Задайте вопрос", "buttonkey4": "❤️ О Нас"}
faqs = {"faq1": "Чем ты можешь мне помочь?", "faq2": "Это бесплатно?", "faq3": "Зачем нужно тестирование?"}
faq_answers = {"faq1": """Со мной ты можешь:
лучше понять свое психологическое состояние, пройдя тестирование
получить рабочие рекомендации по проживаю стресса, способам самопомощи в сложных ситуациях
выбрать себе психолога или смежного специалиста
пройти онлайн-курсы для улучшения навыков совладания со стрессом""",
               "faq2": """Часть моих возможностей являются бесплатными! Некоторые разделы откроются благодаря ежемесячной подписке за небольшую стоимость.
Разработанные квалифицированными психологами онлайн-курсы также являются платными, но они содержат в себе обучающие материалы, которые позволят надолго закрепить навыки совладания со стрессом.""",
               "faq3": """Мое тестирование разработано квалифицированными специалистами, для которых вопрос стресса является ключевым в их практической и научной деятельности.
Прохождение теста позволит вам лучше понять ваше текущее состояние, а также сформировать наиболее подходящие рекомендации. Без тестирования персональные рекомендации сформировать не получится 🥺""",}
courses_slovar = {"course1": "Онлайн-курс «Терапия творчеством» ✨"}


def hello_button():
    builder = ReplyKeyboardBuilder()
    button = KeyboardButton(text=hello_slovar["hello"], request_contact=True)
    builder.row(button)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def gender_keyboard_maker():
    builder = InlineKeyboardBuilder()
    button1 = InlineKeyboardButton(text=hello_slovar["male"], callback_data="male")
    builder.add(button1)
    button2 = InlineKeyboardButton(text=hello_slovar["female"], callback_data="female")
    builder.add(button2)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def yesorno_keyboard_maker():
    builder = ReplyKeyboardBuilder()
    button1 = KeyboardButton(text=yesorno_slovar["yes"])
    builder.add(button1)
    button2 = KeyboardButton(text=yesorno_slovar["no"])
    builder.add(button2)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def menu_keyboard_maker():
    builder = ReplyKeyboardBuilder()
    button1 = KeyboardButton(text=menu_slovar["buttonkey1"])
    builder.row(button1)
    button2 = KeyboardButton(text=menu_slovar["buttonkey2"])
    builder.row(button2)
    button3 = KeyboardButton(text=menu_slovar["buttonkey3"])
    builder.row(button3)
    button4 = KeyboardButton(text=menu_slovar["buttonkey4"], web_app=WebAppInfo(url="https://antistress-bot.bitrix24site.ru/"))
    builder.row(button4)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def faq_keyboard_maker():
    builder = InlineKeyboardBuilder()

    for faq in faqs.keys():
        button = InlineKeyboardButton(text=faqs[faq], callback_data=faq)
        builder.row(button)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def courses_keyboard_maker():
    builder = InlineKeyboardBuilder()

    for course_key in courses_slovar.keys():
        button = InlineKeyboardButton(text=courses_slovar[course_key], callback_data=course_key)
        builder.row(button)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def main_test_keyboard_maker():
    builder = InlineKeyboardBuilder()
    button = InlineKeyboardButton(text="Начать тест", callback_data="main_test")
    builder.row(button)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)
