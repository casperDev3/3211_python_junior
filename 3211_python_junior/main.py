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

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6897684920:AAGQmHQUGpqgTaxxrSXX4R7rHfLcHxpbk5I"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


#### REPLY KEYBOARD MARKUP
def r_main_menu():
    main_menu = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text="Показати під-меню"), KeyboardButton(text="Видалити акаунт 🗑")
    ], [
        KeyboardButton(text="Про нас")
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
