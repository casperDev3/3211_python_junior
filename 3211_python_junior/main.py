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
from aiogram.utils.media_group import MediaGroupBuilder

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6897684920:AAGQmHQUGpqgTaxxrSXX4R7rHfLcHxpbk5I"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
state = {
    "mode": "default"
}  # default, register


#### REPLY KEYBOARD MARKUP
def r_main_menu():
    main_menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Заповнити анкету")],
        [KeyboardButton(text="Показати під-меню"), KeyboardButton(text="Видалити акаунт 🗑")],
        [KeyboardButton(text="Показати інлайн меню")]
    ], resize_keyboard=True)
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
        media_group = MediaGroupBuilder(caption="Media group caption")
        # Add photo
        media_group.add_photo(media="https://picsum.photos/200/300")
        # Dynamically add photo with known type without using separate method
        await bot.send_media_group(chat_id=chat_id, media=media_group.build())
    elif data == "doc":
        # await bot.send_sticker(chat_id, "https://picsum.photos/200/300")
        await bot.send_contact(chat_id, '380969999999', "John")
        # await bot.send_location(chat_id, 32.22345, 35.24851651)
        # await bot.set_chat_title(chat_id, "Test Change Name Chat") # only public channels
        # await bot.send_poll(chat_id, 'test Poll)', ["test1", "test2"], is_anonymous=False,
        #                     allows_multiple_answers=True)
        # await bot.send_chat_action(chat_id, 'record_voice') # only public channels


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=r_main_menu())


@dp.message()
async def echo_handler(message: types.Message, mode=None) -> None:
    try:
        if state["mode"] == "default":
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
            elif message.text == "Заповнити анкету":
                state["mode"] = "register"
                await message.answer("Ви почали запавнювати анкету!")

        elif state["mode"] == "register":
            print("You start REGISTER MODE")
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
