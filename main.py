import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


TOKEN = '7292909718:AAEoFt-ewVh5Z9L6NRDB0PZ4dZ_WEs934X8'

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет это бот Стаса, пока находиться в разработке, здесь ты сможешь покупать машины')


@dp.message()
async def echo(message: types.Message):
    await message.answer('Бот пока находится в разработке')
    user_text = message.text
    await message.answer(user_text)


async def main():
    print('Бот запущен')
    await dp.start_polling(bot)

asyncio.run(main())



