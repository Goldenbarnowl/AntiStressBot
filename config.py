from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from pydantic_settings import BaseSettings

class Secrets(BaseSettings):
    token: str
    bitrix: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


secrets = Secrets()

WEBHOOK_URL = secrets.bitrix

# Инициализация бота
default = DefaultBotProperties(parse_mode='HTML', protect_content=False)
bot = Bot(token= secrets.token, default=default)
dp = Dispatcher()
