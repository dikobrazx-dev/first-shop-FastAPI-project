from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database.database import get_session
from services.user_service import UserService
from repositories.user_repository import UserRepository

def get_user_repository(session: AsyncSession = Depends(get_session)):
    return UserRepository(session)

def get_user_service(user_repo: UserRepository = Depends(get_user_repository)):
    return UserService(user_repo)


from services.product_service import ProductService
from repositories.product_repository import ProductRepository

def get_product_repository(session: AsyncSession = Depends(get_session)):
    return ProductRepository(session)

def get_product_service(product_repo: ProductRepository = Depends(get_product_repository)):
    return ProductService(product_repo)


from services.order_service import OrderService
from repositories.order_repository import OrderRepository

def get_order_repository(session: AsyncSession = Depends(get_session)):
    return OrderRepository(session)

def get_order_service(
    order_repo: UserRepository = Depends(get_order_repository),
    user_service: UserService = Depends(get_user_service),
    product_service: ProductService = Depends(get_product_service)
  ):
    return OrderService(order_repo, user_service, product_service)
