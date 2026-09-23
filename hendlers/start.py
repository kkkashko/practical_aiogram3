from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.reply import ReplyKeyboards
from database.db import Database

def register_start_handlers(dp: Dispatcher):

    @dp.message(Command("start"))
    async def cmd_start(message: Message):

        await Database.add_user(
            user_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name
        )
        
        keyboard = ReplyKeyboards.main_menu() #? Вызов метода для создания главного окна меню

        await message.answer(
            "Привет!\nЯ твой персональный телеграм-бот.\nЧем могу быть полезен?",
            reply_markup=keyboard
        )

    @dp.message(Command("crash"))
    async def cmd_crash(message: Message):
        result = 1 / 0
        await message.answer(str(result))
    
    @dp.message(F.text == "Старт")
    async def handle_start_button(message: Message):

        keyboard = ReplyKeyboards.main_menu() #? Вызов метода для создания главного окна меню

        await message.answer(
            "Я уже здесь!\nЧем могу быть полезен?",
            reply_markup=keyboard
        )

    @dp.message(F.text == "Помощь")
    async def handle_help_button(message: Message):

        await message.answer(
            "ПОМОЩЬ:"
            "Доступные команды: "
            "1. /start - главное меню"
            "2. /photo - показать фото"
            "3. /help - справочный материал"
            "Используй кнопки внизу для навигации!"
        )
