from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from routers.api_users import router as user_router
from routers.api_products import router as product_router
from routers.api_orders import router as order_router
from routers.api_auth import router as auth_router
import exceptions
from exceptions import UserNotFoundError, ProductNotFoundError, OrderNotFoundError, InvalidQuantityError, ServiceError

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(title="Мой интернет магазин",lifespan=lifespan)

@app.exception_handler(UserNotFoundError)
async def user_not_found_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

@app.exception_handler(ProductNotFoundError)
async def product_not_found_handler(request: Request, exc: ProductNotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

@app.exception_handler(OrderNotFoundError)
async def order_not_found_handler(request: Request, exc: OrderNotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

@app.exception_handler(InvalidQuantityError)
async def invalid_quantity_handler(request: Request, exc: InvalidQuantityError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})

@app.exception_handler(ServiceError)
async def service_error_handler(request: Request, exc: ServiceError):
    return JSONResponse(status_code=500, content={"detail": str(exc)})

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(auth_router)

