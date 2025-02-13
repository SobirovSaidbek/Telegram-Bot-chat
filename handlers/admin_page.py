from aiogram.dispatcher import FSMContext

from keyboards.batuon_inline.battuon_inline import contact_admin_def
from main.config import ADMINS
from keyboards.battun.battuon import user_main_menu, phone_number_share, location_share
from load import dp, db, bot
from aiogram import types
from keyboards.batuon_inline.battuon_inline import contact_admin

from states.states import RegisterStates


@dp.message_handler(text="Adminga xabar yuborish")
async def contact_admin_handler(message: types.Message, state: FSMContext):
    text = "Habarni kiriting"
    await message.answer(text=text)
    await state.set_state('contact-admin')


@dp.message_handler(state="contact-admin")
async def contact_admin_handler(message: types.Message, state: FSMContext):
    user = db.get_user_by_chat_id(chat_id=message.chat.id)
    text = f"""
ADMIN => {user[3]}

{message.text}
"""
    await bot.send_message(chat_id=ADMINS, text=text, reply_markup=await contact_admin_def(message.chat.id))
    text = "Habar adminga yuborildi"
    await message.answer(text=text)
    await state.finish()


@dp.callback_query_handler(contact_admin.filter(act='reply'))
async def admin_reply_handler(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await state.update_data(send_chat_id=callback_data['chat_id'])
    text = "Javobingizni kiring"
    await call.message.answer(text=text)
    await state.set_state('admin-reply')


@dp.message_handler(state="admin-reply")
async def admin_reply_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    send_chat_id = data['send_chat_id']
    await bot.send_message(chat_id=send_chat_id, text=message.text)
    text = "Habar yuborildi"
    await message.answer(text=text)
    await state.finish()