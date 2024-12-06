import asyncio
from fastapi import FastAPI
from api.routes.api import router as api_router
from core.events import create_start_app_handler
from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from api import start_telegram_bot  # Импорт функции для запуска бота

def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    pre_load = False
    if pre_load:
        application.add_event_handler("startup", create_start_app_handler(application))
    return application

app = get_application()

# Запуск Telegram-бота
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_telegram_bot())

