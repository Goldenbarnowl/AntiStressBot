from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


hello_slovar = {"hello": "Привет, давай познакомимся 👋", "female": "👩 Женщина‍", "male": "👨 Мужчина"}
yesorno_slovar = {"yes": "Да", "no": "Нет"}
menu_slovar = {"buttonkey1": "👁 Тестирование", "buttonkey2": "💡 Курсы", "buttonkey3": "❓ Задайте вопрос",}
faqs = {"faq1": "Вопрос 1", "faq2": "Вопрос 2", "faq3": "Вопрос 3", "faq4": "Вопрос 4"}
faq_answers = {"faq1": "Ответ 1", "faq2": "Ответ 2", "faq3": "Ответ 3", "faq4": "Ответ 4"}
courses_slovar = {"course1": "Курс 1", "course2": "Курс 2"}


def hello_button():
    builder = ReplyKeyboardBuilder()
    button = KeyboardButton(text=hello_slovar["hello"])
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
