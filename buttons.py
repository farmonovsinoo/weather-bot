from aiogram.types import *


btn = KeyboardButton("🇺🇿 Uzbek - English 🇺🇸")
btn1 = KeyboardButton("🇺🇸 English - Uzbek 🇺🇿")
btn2 = KeyboardButton("🇺🇿 Uzbek - Russian 🇷🇺")
btn3 = KeyboardButton("🇷🇺 Russian - Uzbek 🇺🇿")  
btn4 = KeyboardButton("🇺🇿 Uzbek - China 🇨🇳")
btn5 = KeyboardButton("🇨🇳 China - Uzbek 🇺🇿")
btn8 = KeyboardButton("🇺🇿 Uzbek - Turkish 🇹🇷")
btn9 = KeyboardButton("🇹🇷 Turkish - Uzbek 🇺🇿")
btn13 = KeyboardButton("🇺🇿 Uzbek - Japanese 🇯🇵")
btn14 = KeyboardButton("🇯🇵 Japanese - Uzbek 🇺🇿")
RKM = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btn, btn1, btn2, btn3, btn4, btn5, btn8, btn9, btn13, btn14)

orqaga = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(KeyboardButton("/start"))

ikb = InlineKeyboardButton("➕AZO BO'LISH", url="t.me/Dasturlash_haqida_rasmiy")
IKM = InlineKeyboardMarkup().add(ikb)

ovoz = InlineKeyboardButton("ovoz", callback_data='ovoz')

markup = InlineKeyboardMarkup(row_width=1)
markup.add(
    InlineKeyboardButton("O'zbek", callback_data='uz'),
    InlineKeyboardButton("Русский", callback_data='ru'),
    InlineKeyboardButton("English", callback_data='en'),
)

wiki_lang = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("O'zbek🇺🇿"), KeyboardButton("English🇺🇸"), KeyboardButton("русский🇷🇺"),
)

menus = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
menus.add(
        KeyboardButton("Tarjima"), KeyboardButton("Kalkulyaotr"),
        KeyboardButton("YouTubedan video yuklash"), KeyboardButton("Instagramdan video yuklash"),
        KeyboardButton("wikipedia"),KeyboardButton("Kiril va Lotin") , KeyboardButton("izoh qoldirish")
    )

kirillatin = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("krildan loringa"), KeyboardButton("lotindan krilga")
)