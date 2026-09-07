import os 

from aiogram import Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

def register_photo_handlers(dp: Dispatcher):

    @dp.message(Command("photo")) 
    async def cmd_photo(message: Message):

        await message.answer("Фото отправляется...")

        photo_path = os.path.join("core/img", "1.jpg")

        if not os.path.exists(photo_path):
            await message.answer("Ошибка, фото не существует!...")
            
            return

        photo = FSInputFile(photo_path)

        await message.answer_photo(
            photo=photo,
            caption="Вот ваш Николас Кейдж!"
        )

    @dp.message(F.text == "Фото")
    async def handle_photo_btn(message: Message):

        await cmd_photo(message)