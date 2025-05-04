import asyncio
from aiogram import Bot, Dispatcher, types


TOKEN = '7292909718:AAGN_ujZ5YSV-SXtbxRh-9Y_GPDfTuHnYQo'

bot = Bot(token=TOKEN)
dp = Dispatcher()


from handlers.user_privat import user_router
from handlers.user_group import group_router
dp.include_router(user_router)
dp.include_router(group_router)

async def main():
    print('Бот запущен')
    await dp.start_polling(bot)

asyncio.run(main())



