from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton  #? ДЛЯ работы с обчными клавиатурами

class ReplyKeyboards:

    @staticmethod
    def main_menu():

        btn_start = KeyboardButton(text="Старт")
        btn_photo = KeyboardButton(text="Фото")
        btn_help = KeyboardButton(text="Помощь")

        keyboard = ReplyKeyboardMarkup(
            keyboard=[[btn_start, btn_photo], [btn_help]],
            resize_keyboard=True,
            one_time_keyboard=False,
        )

        return keyboard

    @staticmethod
    def photo_menu(): #? Создает клаву для меню фото

        btn_random = KeyboardButton(text="Случайное фото")
        btn_cnl = KeyboardButton(text="Назад")

        keyboard = ReplyKeyboardMarkup(
            keyboard=[[btn_random], [btn_cnl]],
            resize_keyboard=True,
            one_time_keyboard=False,
        )

        return keyboard

    @staticmethod
    def remove():
        return ReplyKeyboardRemove()
