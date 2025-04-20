from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет это бот Стаса, пока находиться в разработке, здесь ты сможешь покупать машины')


@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer('Каталог в котором в скором времени будут товары')


@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('Бот для продажи авто по Беларуси')


@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer('Контакты: +375339009914')


@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer('Ул. Пушкина д. Калатушкина')


@user_router.message()
async def echo(message: types.Message):
    await message.answer('Бот пока находится в разработке')
    user_text = message.text
    await message.answer(user_text)