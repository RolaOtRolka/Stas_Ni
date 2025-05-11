from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_btn = KeyboardButton(text='Назад')


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог'), KeyboardButton(text='Про нас')],
        [KeyboardButton(text='Контакт'), KeyboardButton(text='Адрес')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Нажмите на кнопку ниже...'
)


catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Daewoo Matiz'), KeyboardButton(text='BMW E34')],
        [KeyboardButton(text='Boeing 737'), KeyboardButton(text='Lamborgini Urus')],
        [KeyboardButton(text='Ferrari F40'), KeyboardButton(text='Porshe 911')],
        [back_btn]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите товар...'
)