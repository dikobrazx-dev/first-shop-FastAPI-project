from fastapi import FastAPI

from routers.api_users import router as user_router
from routers.api_products import router as product_router
from routers.api_orders import router as order_router
import exceptions

app = FastAPI(title="Мой интернет магазин")

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)

