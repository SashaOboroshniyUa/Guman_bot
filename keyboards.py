from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choice_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Підтримка Військових"),
     KeyboardButton(text="Підтримка Тварин"),
     KeyboardButton(text="Ідеї")]
])
