import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from googletrans import Translator
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command
from aiogram.dispatcher.filters import Text
from buttons import *
import os
import glob
from gtts import gTTS
from pytube import YouTube
import instaloader
import wikipedia
import asyncio
from transliterate import to_cyrillic, to_latin

API_TOKEN = '5904607271:AAHpGjgqnwtTxbDy-Bq7pzNI-Br8nS11tlE'
channel_id  ='-1001781579548'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class krilotin(StatesGroup):
    knopka = State()
    transliterate = State()

class Menu(StatesGroup):
    first = State()

class Insta(StatesGroup):
    insta = State()

class Wiki(StatesGroup):
    wiki = State()
    pedia = State()

class youtube(StatesGroup):
    down = State()

class calculator(StatesGroup):
    calc = State()

class Translate(StatesGroup):
    lang = State()
    trans = State()

@dp.message_handler(CommandStart(), state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply(f"salom {message.from_user.full_name}\nmen universal botman\nkerakli menuni tanlang", reply_markup=menus)
    await Menu.first.set()

@dp.message_handler(state=Menu.first)
async def tarjima(message: types.Message, state: FSMContext):
    await state.update_data({'menu': message.text})
    data = await state.get_data()
    www = data.get("menu")
    if www == "Tarjima":
        await message.answer("kerakli tugmani tanlang", reply_markup=RKM)
        await Translate.lang.set()
    elif www == "Kalkulyaotr":
        await message.answer("Menga matematik misol yuboring")
        await calculator.calc.set()
    elif www == "YouTubedan video yuklash":
        await message.answer("Menga youtubedagi video linkini yuboring video yuboring")
        await youtube.down.set()
    elif www == "Instagramdan video yuklash":
        await message.answer("Menga instagramdan video linkini yuboring")
        await Insta.insta.set()
    elif www == "wikipedia":
        await message.answer("tilni tanlang", reply_markup=wiki_lang)
        await state.update_data({'wiki': message.text})
        await Wiki.wiki.set()
    elif www == "Kiril va Lotin":
        await message.answer("tugmalardan birini tanlang", reply_markup=kirillatin)
        await krilotin.knopka.set()

@dp.message_handler(state=krilotin.knopka)
async def krillatin(message: types.Message, state: FSMContext):
    await message.answer("menga so'z yuboring")
    await krilotin.transliterate.set()

@dp.message_handler(state=krilotin.transliterate)
async def transliterator(message: types.Message, state: FSMContext):
    await state.update_data({'kiril': message.text})
    data = await state.get_data()
    find = data.get("kiril")
    if find == "krildan loringa":
        await message.answer(to_cyrillic(message.text), reply_markup=orqaga)
        await krilotin.transliterate.set()
    elif find == "lotindan krilga":
        await message.answer(to_latin(message.text), reply_markup=orqaga)
        await krilotin.transliterate.set()

@dp.message_handler(state=calculator.calc)
async def Calc(message: types.Message, state: FSMContext):
    await state.update_data({'calc': message.text})
    data = await state.get_data()
    calc = data.get("calc")
    if '×' in calc:
        await message.answer(eval(calc.replace('×', '*')), reply_markup=orqaga)
        await calculator.calc.set()
    elif '÷' in calc:
        await message.answer(eval(calc.replace('÷', '/')), reply_markup=orqaga)
        await calculator.calc.set()
    else:
        await message.answer(eval(calc), reply_markup=orqaga)
        await calculator.calc.set()

@dp.message_handler(state=Translate.trans)
async def translate_text(message: types.Message, state: FSMContext):
    data = await state.get_data()

@dp.message_handler(state=Wiki.wiki)
async def wikipedia(message: types.Message, state: FSMContext):
    await message.answer("menga so'z yuboring")
    await Wiki.pedia.set()

@dp.message_handler(state=Wiki.pedia)
async def wikipedia(message: types.Message, state: FSMContext):
    await state.update_data({'wiki': message.text})
    data = await state.get_data()
    www = data.get("wiki")
    if www == "O'zbek":
        await message.answer(wikipedia.summary(www))
        await Menu.first.set()
    elif www == "English":
        await message.answer(wikipedia.summary(www))
        await Menu.first.set()
    elif www == "Русский":
        await message.answer(wikipedia.summary(www))
        await Menu.first.set()

@dp.message_handler(state=Insta.insta)
async def instagram_down(message: types.Message, state: FSMContext):
    await message.answer("video yuklanmoqda...")
    loader = instaloader.Instaloader()
    loader.download_profile(message.text, profile_pic_only=True)
    with open(str(message.text)) as photos:
        await message.answer_photo(photo=photos, caption=f"{message.text}", reply_markup=menus)
        os.remove(message.text)
    # await message.answer("Video yuklashda xatolik yuz berdi")

@dp.message_handler(state=youtube.down)
async def youtube_down(message: types.Message, state: FSMContext):
    try:
        await message.answer("video yuklanmoqda...")
        yt = YouTube(message.text.strip())
        video = yt.streams.get_highest_resolution()
        audio = yt.streams.filter(only_audio=True).last()
        video.download(output_path="videos")
        video_files = glob.glob("videos/*.mp4")
        video_files.sort(key=os.path.getctime)
        last_video = video_files[-1]
        with open(str(last_video), 'rb') as videos:
            await asyncio.sleep(2)
            await message.answer_video(video=videos, caption=f"{yt.title}", reply_markup=menus)
        audio.download(output_path="audios")
        audio_files = glob.glob("audios/*.webm")
        audio_files.sort(key=os.path.getctime)
        last_audio = audio_files[-1]
        with open(str(last_audio), 'rb') as audio:
            await message.answer_voice(voice=audio)
            await Menu.first.set()
    except:
        await message.answer("Video yuklashda xatolik yuz berdi")

@dp.message_handler(state=Translate.lang)
async def which_lang(message: types.Message, state: FSMContext):
    lang = message.text
    await state.update_data({'lang': lang})
    await message.answer("tarjima qilish uchun so'z kiriting\norqaga qaytish uchun /start buyrug'ini bosing", reply_markup=orqaga)
    await Translate.next()
        
@dp.message_handler(state=Translate.trans)
async def translate_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang")
    text = message.text
    tarjimon = Translator() 
    if lang == "🇺🇿 Uzbek - English 🇺🇸":
        tarjima = tarjimon.translate(text, dest='en')
        await message.answer(tarjima.text, reply_markup=orqaga)
        voice = gTTS(text=tarjima.text, lang='en')
        voice.save("voice.mp3")
        with open("voice.mp3", "rb") as voice:
            await message.answer_voice(voice=voice)
        os.remove("voice.mp3")
    elif lang == "🇺🇸 English - Uzbek 🇺🇿":
        tarjima = tarjimon.translate(text, dest='uz')
        await message.answer(tarjima.text, reply_markup=orqaga)
    elif lang == "🇺🇿 Uzbek - Russian 🇷🇺":
        tarjima = tarjimon.translate(text, dest='ru')
        await message.answer(tarjima.text, reply_markup=orqaga)
        voice = gTTS(text=tarjima.text, lang='ru')
        voice.save("voice.mp3")
        with open("voice.mp3", "rb") as voice:
            await message.answer_voice(voice=voice)
        os.remove("voice.mp3")
    elif lang == "🇷🇺 Russian - Uzbek 🇺🇿":
        tarjima = tarjimon.translate(text, dest='uz')
        await message.answer(tarjima.text, reply_markup=orqaga)
    elif lang == "🇺🇿 Uzbek - China 🇨🇳":
        tarjima = tarjimon.translate(text, dest='zh-cn')
        await message.answer(tarjima.text, reply_markup=orqaga)
        voice = gTTS(text=tarjima.text, lang='zh-cn')
        voice.save("voice.mp3")
        with open("voice.mp3", "rb") as voice:
            await message.answer_voice(voice=voice)
        os.remove("voice.mp3")
    elif lang == "🇨🇳 China - Uzbek 🇺🇿":
        tarjima = tarjimon.translate(text, dest='uz')
        await message.answer(tarjima.text, reply_markup=orqaga)
    elif lang == "🇺🇿 Uzbek - Turkish 🇹🇷":
        tarjima = tarjimon.translate(text, dest='tr')
        await message.answer(tarjima.text, reply_markup=orqaga)
        voice = gTTS(text=tarjima.text, lang='tr')
        voice.save("voice.mp3")
        with open("voice.mp3", "rb") as voice:
            await message.answer_voice(voice=voice)
        os.remove("voice.mp3")
    elif lang == "🇹🇷 Turkish - Uzbek 🇺🇿":
        tarjima = tarjimon.translate(text, dest='uz')
        await message.answer(tarjima.text, reply_markup=orqaga)
    elif lang == "🇺🇿 Uzbek - Japanese 🇯🇵":
        tarjima = tarjimon.translate(text, dest='ja')
        await message.answer(tarjima.text, reply_markup=orqaga)
        voice = gTTS(text=tarjima.text, lang='ja')
        voice.save("voice.mp3")
        with open("voice.mp3", "rb") as voice:
            await message.answer_voice(voice=voice)
        os.remove("voice.mp3")
    elif lang == "🇯🇵 Japanese - Uzbek 🇺🇿":
        tarjima = tarjimon.translate(text, dest='uz')
        await message.answer(tarjima.text, reply_markup=orqaga)
    else:
        await message.answer(message.text, reply_markup=orqaga)
    await Translate.trans.set()

@dp.message_handler(state=calculator.calc)
async def Calc(message: types.Message, state: FSMContext):
    await state.update_data({'calc': message.text})
    data = await state.get_data()
    calc = data.get("calc")
    if '×' in calc:
        await message.answer(eval(calc.replace('×', '*')), reply_markup=orqaga)
        await calculator.calc.set()
    elif '÷' in calc:
        await message.answer(eval(calc.replace('÷', '/')), reply_markup=orqaga)
        await calculator.calc.set()
    else:
        await message.answer(eval(calc), reply_markup=orqaga)
        await calculator.calc.set()

@dp.message_handler()
async def echo(message: types.Message):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)