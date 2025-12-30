import json
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "ТОКЕН_ТВОЕГО_НОВОГО_БОТА"

bot = Bot(token=TOKEN)
dp = Dispatcher()
app = FastAPI()

# Команда /app — открыть WebApp
@dp.message(Command("app"))
async def open_app(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть приложение 🎲",
                    web_app=WebAppInfo(url="https://ТВОЙ-ПРОЕКТ.vercel.app/webapp")
                )
            ]
        ]
    )
    await message.answer("Открываю приложение:", reply_markup=keyboard)

# Приём данных из WebApp
@dp.message()
async def handle_webapp(message: types.Message):
    if not message.web_app_data:
        return

    data = json.loads(message.web_app_data.data)
    action = data.get("action")

    if action == "join":
        await message.answer("🙋 Ты участвуешь!")
    elif action == "random":
        await message.answer("🎲 Выбираю победителя...")

# Webhook endpoint
@app.post("/api/index.py")
async def telegram_webhook(request: Request):
    update = await request.json()
    await dp.feed_update(bot, update)
    return {"ok": True}
