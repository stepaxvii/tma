from os import getenv
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher
from aiogram.types import Update
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from tortoise.contrib.fastapi import register_tortoise

from bot.start_app import router
from config import TORTOISE_ORM


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


@app.post("/tma" + WEBHOOK_PATH)
async def webhook(request: Request):
    try:
        update = Update.model_validate(
            await request.json(), context={"bot": bot}
        )
        await dp.feed_update(bot, update)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/tma")
async def tma_root():
    return {"message": "Welcome to TMA!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
