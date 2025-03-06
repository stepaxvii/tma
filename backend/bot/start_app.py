from aiogram import types
from aiogram import Router
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def handler_command_start(message: types.Message):
    await message.answer(
        text=(
            "Добро пожаловать)"
        ),
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[
            types.InlineKeyboardButton(
                text="Открыть приложение.",
                web_app=types.WebAppInfo(
                    url="https://stepaxvii.store/tma"
                )
            )
        ]])
    )
