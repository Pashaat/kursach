import json
import logging
import requests
from bs4 import BeautifulSoup
import buttons
import config
import parse
import TOKEN
import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import bold

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ParseMode, KeyboardButton, CallbackQuery

from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

class StateMachine(StatesGroup):
    region_state = State()
    city_state = State()
    what_city_state = State()
    without_city_state = State()
    product_name_state = State()
    show_state = State()

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=TOKEN.token)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

conn = sqlite3.connect('all_info.db')
cur = conn.cursor()


@dp.message_handler(commands=['start'], state='*')
async def start(massage: types.Message):
    await massage.answer("Привет!", reply_markup=buttons.greet_kb)

@dp.message_handler(lambda a: a.text == 'Выбрать область', state='*')
async def oblast_choise(message: types.Message):
    await message.answer(f"Введите цифру области:\n1.Вся Беларусь\n2.Минск\n3.Брестская\n4.Гомельская\n5.Гродненская\n"
                         f"6.Могилёвская\n7.Минская\n8.Витебская")
    await StateMachine.region_state.set()


@dp.message_handler(state=StateMachine.region_state)
async def what_oblast_choise(message: types.Message):
    if message.text == '1':
        with open('data.txt', 'w', encoding='UTF-8') as k:
            k.write('1;;#;#;')
            await message.answer(f'Вы выбрали {config.oblasty[message.text]}')
            await message.answer('Введите название товара')
            await StateMachine.product_name_state.set()
    else:
        await message.answer(f'Вы выбрали {config.oblasty[message.text]}', reply_markup=buttons.withorwithout)
        await StateMachine.city_state.set()
        with open('data.txt', 'w', encoding='UTF-8') as f:
            f.write(f'{message.text};{config.oblasty_kuf[message.text]};')



@dp.message_handler(state=StateMachine.city_state)
async def city_choise(message: types.Message):
    if message.text == 'Выбрать город/район':
        with open('data.txt', 'r', encoding='UTF-8') as f:
            a = f.readline()
            a.replace(';', '')
            citys = []
            oblast = a[0]
            for key, value in config.citys[oblast].items():
                citys.append(f'{key}.{value}')
            await message.answer('\n'.join(citys))
            await StateMachine.what_city_state.set()
    elif message.text == 'Продолжить без города':
        with open('data.txt', 'a', encoding='UTF-8') as k:
            k.write('#;#;')
        await message.answer('Введите название товара')
        await StateMachine.product_name_state.set()

@dp.message_handler(state=StateMachine.what_city_state)
async def what_city_choise(message: types.Message):
    with open('data.txt', 'a', encoding='UTF-8') as k:
        with open('data.txt', 'r', encoding='UTF-8') as f:
            a = f.readline()
            a.replace(';', '')
            k.write(f'{message.text};{config.citys_cuf[a[0]][message.text]};')
            await message.answer(f'Вы выбрали {config.citys[a[0]][message.text]}')
    await StateMachine.product_name_state.set()
    await message.answer('Введите название товара')


@dp.message_handler(state=StateMachine.product_name_state, content_types='text')
async def what_product(message: types.Message):
    with open('data.txt', 'a', encoding='UTF-8') as k:
        k.write(f'{message.text};')
    parse.run_parse()
    await message.answer('Результаты готовы', reply_markup=buttons.wiew_results_button)
    await StateMachine.show_state.set()

@dp.message_handler(lambda a: a.text == 'Показать результаты' , state=StateMachine.show_state)
async def show(message: types.Message):
    cur.execute("SELECT * FROM info;")
    all_results = cur.fetchall()
    for i in all_results:
        await bot.send_photo(chat_id=message.chat.id, photo=f'{i[3]}', caption=f'{i[1]}\nЦена:{i[2]}\n{i[4]}')

executor.start_polling(dp)