import logging 
import time
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject

logger = logging.getLogger(__name__)

class LoggingMiddleWare(BaseMiddleware): #? Класс для работы с мидлварами (обработка входящих сообщений)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any], Awaitable[Any]]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        user = None 
        if isinstance(event, Message):
            user = event.from_user #? Передача юзера
        elif isinstance(event, CallbackQuery): 
            user = event.from_user #? Передача юзера

        user_info = f"{user.id} (@{user.username})" if user else "Неизвестный пользователь"
        logger.info(f"Входящее сообытие от {user_info}")

        start = time.time()

        result = await handler(event, data)

        time_result = time.time() - start
        logger.info(f"Обработано за {time_result:.2f} сек")

        return result

