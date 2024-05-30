from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterStates(StatesGroup):
    full_name = State()
    username = State()
    phone_number = State()
    location = State()