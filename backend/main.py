from os import getenv
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher
from aiogram.types import Update
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from tortoise.contrib.fastapi import register_tortoise

from backend.bot.start_app import router
from backend.config import TORTOISE_ORM


load_dotenv()

TELEGRAM_TOKEN_BOT = getenv('TELEGRAM_TOKEN_BOT')
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = "https://stepaxvii.store/tma" + WEBHOOK_PATH

bot = Bot(token=TELEGRAM_TOKEN_BOT)
dp = Dispatcher()

dp.include_router(router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await bot.set_webhook(WEBHOOK_URL)
    yield
    await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)


register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


# Обработчик вебхука для FastAPI
@app.post(WEBHOOK_PATH)
async def webhook(request: Request):
    try:
        # Получаем данные из запроса
        update = Update.model_validate(
            await request.json(), context={"bot": bot}
        )
        # Обрабатываем обновление через диспетчер
        await dp.feed_update(bot, update)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Дополнительные маршруты для главного приложения
@app.get("/")
async def root():
    return {"message": "Hello, Hello! World!"}

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
