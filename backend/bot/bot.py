# import asyncio
# import logging
# import sys
# from os import getenv

# from dotenv import load_dotenv
# from aiogram import Bot, Dispatcher
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode

# from backend.bot.start_app import router

# load_dotenv()

# TELEGRAM_TOKEN_BOT = getenv('TELEGRAM_TOKEN_BOT')


# async def main():
#     bot = Bot(
#         token=TELEGRAM_TOKEN_BOT,
#         default=DefaultBotProperties(parse_mode=ParseMode.HTML)
#     )
#     dp = Dispatcher()
#     dp.include_routers(router)

#     try:
#         await bot.delete_webhook(drop_pending_updates=True)
#         await dp.start_polling(bot)
#     except Exception as error:
#         logging.error(f'Произошла ошибка: {error}')


# if __name__ == "__main__":
#     logging.basicConfig(
#         level=logging.INFO,
#         stream=sys.stdout,
#     )
#     asyncio.run(main())
