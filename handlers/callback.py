from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp

async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton("TEXT", callback_data="button2")
    markup.add(button2)
    question = "By whom invented Python?"
    answer = [
        'Bjorn Stroustrup',
        'Guido Van Rossum',
        'Scott Wiltamut and Anders Heilsberg',
        'James Gosling',
        'Mitchell Reznik',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        correct_option_id=1,
        reply_markup=markup,
        type="quiz"   
    )

async def quiz3(call: types.CallbackQuery):
    question = "How long did World War 1 last?"
    answer = [
        '4 years',
        '3 years',
        '7 years',
        '1 year',
        '10 years',
        '5 years',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, lambda call: call.data == "button1")
    dp.register_callback_query_handler(quiz3, lambda call: call.data == "button2")