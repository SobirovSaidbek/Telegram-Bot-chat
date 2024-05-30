from aiogram.dispatcher import FSMContext

from keyboards.battun.battuon import user_main_menu, phone_number_share, location_share
from load import dp, db
from aiogram import types
from states.states import RegisterStates

@dp.message_handler(commands=['start'])
async def user_start(message: types.Message):
    if db.get_user(chat_id=message.chat.id):
        text = "Assalomu alaykum xush kelibsz"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = f"""
            Assalomu alaykum 🙋🏼‍♂️
xush kelibsz 😊
Ismingizni kiriting ✔
        """
        await message.answer(text=text)
        await RegisterStates.full_name.set()


@dp.message_handler(state=RegisterStates.full_name)
async def full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text, chat_id=message.chat.id)
    text="Telfon Ramingizni Kiriting 📲"
    await message.answer(text=text, reply_markup=phone_number_share)
    await RegisterStates.phone_number.set()


@dp.message_handler(state=RegisterStates.phone_number, content_types=types.ContentTypes.CONTACT)
async def phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    text="Manzil Location 📍"
    await message.answer(text=text, reply_markup=location_share)
    await RegisterStates.location.set()

@dp.message_handler(state=RegisterStates.location, content_types=types.ContentTypes.LOCATION)
async def location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.text)

    data= await state.get_data()
    if db.add_user(data):
        text = "Muvafaqiyatli qoshildi  ✅"
    else:
        text = "Xalotik bor ❌"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()
