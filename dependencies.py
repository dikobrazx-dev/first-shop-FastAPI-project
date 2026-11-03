from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timezone

from database.database import get_session
from services.user_service import UserService
from repositories.user_repository import UserRepository
from auth import SECRET_KEY, ALGORITHM, oauth2_scheme
from models.user import User
import exceptions


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
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось подтвердить учётные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await user_service.get_user(int(user_id))
    if user is None:
        raise credentials_exception
    return user
