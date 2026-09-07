import asyncio #? Для асинхронной работы
import logging

from aiogram import Bot, Dispatcher, F #? Основные классы для работы с ботом
from aiogram.filters import Command #? для обработки комманд
from aiogram.types import Message, FSInputFile #? Для работы с сообщениями и файлами

from config import BotConfig
from hendlers import register_all_handlers


class TelegramBot:

    def __init__(self):
        
        logging.basicConfig(level=logging.INFO)

        self.token = BotConfig.get_token()

        self.bot = Bot(token=self.token)

        self.dp = Dispatcher()

        register_all_handlers(self.dp)

        logging.info("бот инициализирован...")

    async def start(self):

        bot_info = await self.bot.me()

        print(f"Бот запущен!\nИмя бота: {bot_info.first_name}\nUsername: {bot_info.username}\nID: {bot_info.id}")

        await self.dp.start_polling(self.bot, skip_updates=True)

async def main():

    bot = TelegramBot()

    await bot.start()

if __name__  == "__main__":
    asyncio.run(main())

