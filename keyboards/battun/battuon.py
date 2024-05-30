from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Chatni boshlash"),
        ],
        [
            KeyboardButton(text="Admin page")
        ],
        [
            KeyboardButton(text="Adminga xabar yuborish")
        ]
    ], resize_keyboard=True
)


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



phone_number_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqam jo'natish", request_contact=True)
        ]
    ], resize_keyboard=True
)

location_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzilni jo'natish", request_location=True)
        ]
    ], resize_keyboard=True
)