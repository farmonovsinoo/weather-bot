import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bs4 import BeautifulSoup as bs
from function import Toshkent, Buxoro

######## choosa language button #####################
markup = InlineKeyboardMarkup(row_width=1)
btn = InlineKeyboardButton("Uzbek 🇺🇿", callback_data='uzb')
btn1 = InlineKeyboardButton("English 🇺🇸", callback_data='eng')
btn2 = InlineKeyboardButton("россия 🇷🇺", callback_data='rus')
markup.add(btn, btn1, btn2)
########################################################

################# choose cities button #################
cities = InlineKeyboardMarkup(row_width=2)
cbt = InlineKeyboardButton("Toshkent", callback_data='tosh')
cbb = InlineKeyboardButton("Buxoro", callback_data='bux')
cities.add(cbt, cbb)
########################################################

API_TOKEN = "6485159336:AAHwEtABgpNu5Tm-xzmmmIaVOFyQAQhvHe8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"choose language | tilni tanlang | выбрать язык", reply_markup=markup)

@dp.callback_query_handler(text=['uzb', 'eng', 'rus'])
async def eng_uzb_rus(call: types.CallbackQuery):
    if call.data == 'uzb':
        await call.message.answer("tanang", reply_markup=cities)
    elif call.data == 'eng':
        await call.message.answer("english", reply_markup=cities)
    elif call.data == 'rus':
        await call.message.answer("russia", reply_markup=cities)

@dp.callback_query_handler(text=['tosh', 'bux'])
async def cities_func(call: types.CallbackQuery):
    if call.data == 'tosh':
        await call.message.answer(f"Bugun havo {Toshkent()} bo'ladi")
    elif call.data == 'bux':
        await call.message.answer(f"Bugun havo {Buxoro()} bo'ladi")
        

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)