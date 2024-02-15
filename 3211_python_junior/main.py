import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6897684920:AAGQmHQUGpqgTaxxrSXX4R7rHfLcHxpbk5I"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


#### REPLY KEYBOARD MARKUP
def r_main_menu():
    main_menu = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text="Показати під-меню"), KeyboardButton(text="Видалити акаунт 🗑")
    ], [
        KeyboardButton(text="Показати інлайн меню")
    ]], resize_keyboard=True)
    return main_menu


def r_sub_menu():
    sub_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Item1"), KeyboardButton(text="Item2")],
            [KeyboardButton(text="Item3")],
            [KeyboardButton(text="Item4"), KeyboardButton(text="Item5"), KeyboardButton(text="Item6")],
            [KeyboardButton(text="НАЗАД")]
        ],
        resize_keyboard=True
    )
    return sub_menu


#### INLINE KEYBOARD MARKUP
def i_test_menu():
    test_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Текст", callback_data="txt"),
             InlineKeyboardButton(text="Картинка", callback_data="img")],
            [InlineKeyboardButton(text="Документ", callback_data="doc")]
        ]
    )
    return test_menu


@dp.callback_query(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    chat_id = callback_query.from_user.id
    if data == "txt":
        await bot.send_message(chat_id, "You press Option 1")
    elif data == "img":
        media = open('media/barbie.png', 'rb')
        await bot.send_document(chat_id, media, caption="test")
        media.close()
    elif data == "doc":
        await bot.send_message(chat_id, "You press Option 3")


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=r_main_menu())


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)

        if message.text == "3211":
            await message.answer('Я знаю, це ваша група!')
        elif message.text == "Мій профіль 🥷":
            await message.answer("Ви перейшли в свій профіль!")
        elif message.text == "Показати під-меню":
            await message.answer("Ви перейшли в під-меню!", reply_markup=r_sub_menu())
        elif message.text == "НАЗАД":
            await message.answer("Ви в головному меню!", reply_markup=r_main_menu())
        elif message.text == "Показати інлайн меню":
            await message.answer("Меню, що знаходиться під цим повідомлення - є інлайновим",
                                 reply_markup=i_test_menu())
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
