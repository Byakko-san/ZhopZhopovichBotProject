from os import getenv
import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
LOCAL_PROXY = getenv("LOCAL_PROXY")
session = AiohttpSession(proxy=LOCAL_PROXY)

dp = Dispatcher()
router = Router()
dp.include_router(router)


@router.message()
async def hello(message):
    await message.answer("Hello")

async def main():
    bot = Bot(token=TOKEN, session=session)

    print("START...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())