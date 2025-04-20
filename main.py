import asyncio
from aiogram import Bot, Dispatcher, types


TOKEN = '7292909718:AAEoFt-ewVh5Z9L6NRDB0PZ4dZ_WEs934X8'

bot = Bot(token=TOKEN)
dp = Dispatcher()


from handlers.user_privat import user_router
dp.include_router(user_router)


async def main():
    print('Бот запущен')
    await dp.start_polling(bot)

asyncio.run(main())



