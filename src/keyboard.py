from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

menu_slovar = {"buttonkey1": "Тестирование", "buttonkey2": "Курсы", "buttonkey3": "FAQ",}
faqs = {"faq1": "Вопрос 1", "faq2": "Вопрос 2", "faq3": "Вопрос 3", "faq4": "Вопрос 4"}
faq_answers = {"faq1": "Ответ 1", "faq2": "Ответ 2", "faq3": "Ответ 3", "faq4": "Ответ 4"}
courses_slovar = {"course1": "Курс 1", "course2": "Курс 2", "course3": "Курс 3", "course4": "Курс 4"}

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