from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    hello = State()
    gender = State()
    age = State()
    swo_family = State()
    swo_family_role = State()
    menu = State()
    main_test = State()


class SpielbergerTest(StatesGroup):
    st_answers = State()      # список из 20 ответов (1-4)
    lt_answers = State()      # список из 20 ответов (1-4)
    waiting_st_answer = State()
    waiting_lt_answer = State()

