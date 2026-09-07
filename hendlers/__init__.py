from aiogram import Dispatcher

from .start import register_start_handlers
from .photo import register_photo_handlers

def register_all_handlers(dp: Dispatcher):

    register_start_handlers(dp)

    register_photo_handlers(dp)

    print("все обработчики зарегестрированы!")