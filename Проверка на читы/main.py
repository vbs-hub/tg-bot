import asyncio
from aiogram import Bot, Dispatcher
from handlers import bay_pizza, msg_admin, catalog_pizza

API = 'TOKEN'

bot = Bot(API)
dp = Dispatcher()
dp.include_routers(
    bay_pizza.r,
    msg_admin.r,
    catalog_pizza.r
)

async def main():
    print('Starting BOT...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())