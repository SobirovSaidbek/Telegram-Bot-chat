from aiogram.dispatcher import FSMContext

from keyboards.battun.battuon import user_main_menu
from keyboards.batuon_inline.battuon_inline import user_follow, follow_inline_button, yes_or_no
from load import dp, db, bot
from aiogram import types

from states.states import RegisterStates


@dp.message_handler(text='Chatni boshlash')
async def user_search(message: types.Message, state: FSMContext):
    text = "Id ni kirit"
    await message.answer(text=text)
    await state.set_state('user-search')


@dp.message_handler(state="user-search")
async def get_user_by_id(message: types.Message, state: FSMContext):
    user = db.get_user_by_chat_id(chat_id=int(message.text))
    if user:
        text = "🆔 ni kiriting:"
        await message.answer(text=text, reply_markup=await follow_inline_button(chat_id=user[1]))
    else:
        text = "User topilmadi"
        await message.answer(text=text)
    await state.finish()


@dp.callback_query_handler()
async def follow_user(call: types.CallbackQuery, state: FSMContext):
    user_chat_id = call.data
    chat_id = call.message.chat.id
    user=db.get_user_by_chat_id(chat_id=chat_id)

    await bot.send_message(chat_id=user_chat_id, text=f"Ushbu foydalanuvchi sizga follow bosdi {user[3]}",
                           reply_markup=await yes_or_no(chat_id))



@dp.message_handler(text="Admin page")
async def admin_page(message: types.Message, state: FSMContext):
    text = """
    Assalomu alaykum Shikoyat va murojatlar uchun
ADMIN => http://myurls.co/saidbe_e05
ADMIN 24/7 ishlidi !
    """
    await message.answer(text=text,)