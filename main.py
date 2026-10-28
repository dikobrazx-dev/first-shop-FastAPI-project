from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.database import create_tables,drop_tables
from routers.api_users import router as user_router
from routers.api_products import router as product_router
from routers.api_orders import router as order_router
import exceptions

@asynccontextmanager
async def lifespan(app: FastAPI):
    print ("Старт сервера: Создание таблиц...")
    await create_tables()
    yield
    print("Выключение сервера: Удаление таблиц...")
    await drop_tables()

app = FastAPI(title="Мой интернет магазин",lifespan=lifespan)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)

