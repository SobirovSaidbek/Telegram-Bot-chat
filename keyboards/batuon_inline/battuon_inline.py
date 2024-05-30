from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


user_like_data = CallbackData('like', 'act', 'photo_id')
user_dislike_data = CallbackData('dislike', 'act', 'photo_id')


async def user_follow(username):
    user_follow_1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f" ПОДПИСАТЬСЯ ✅", callback_data=username),
                InlineKeyboardButton(text=f"НЕ ПОДПИСЫВАТЬСЯ ❌", callback_data=username)
            ]
        ]
    )
    return user_follow_1

async def follow_inline_button(chat_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Follow", callback_data=chat_id)
            ]
        ]
    )
    return markup


async def yes_or_no(chat_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"ПОДПИСАТЬСЯ ✅", callback_data=chat_id),
                InlineKeyboardButton(text=f"НЕ ПОДПИСЫВАТЬСЯ ❌", callback_data=chat_id),
            ]
        ]
    )
    return markup


contact_admin = CallbackData('reply', 'act', 'chat_id')
async def contact_admin_def(chat_id):
    contact_admin_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Reply", callback_data=contact_admin.new(act="reply", chat_id=chat_id))
            ]
        ]
    )
    return contact_admin_button