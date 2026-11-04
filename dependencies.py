from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
import jwt, exceptions
from config import settings
from database.database import get_session
from services.user_service import UserService
from repositories.user_repository import UserRepository
from auth import oauth2_scheme
from models.user import User
from exceptions import credentials_exception


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
    order_repo: OrderRepository = Depends(get_order_repository),
    user_service: UserService = Depends(get_user_service),
    product_service: ProductService = Depends(get_product_service)
):
    return OrderService(order_repo, user_service, product_service)


def get_pagination_params(
    skip: int = 0,
    limit: int = 100
):
    from schemas import PaginationParams
    return PaginationParams(skip=skip, limit=limit)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_service: UserService = Depends(get_user_service)
) -> User:
    try:
        payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except :
        raise credentials_exception

    user = await user_service.get_user(int(user_id))
    if user is None:
        raise credentials_exception
    return user
