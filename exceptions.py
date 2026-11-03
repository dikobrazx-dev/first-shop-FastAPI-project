from fastapi import HTTPException, status

class ServiceError(Exception):
    pass

class UserNotFoundError(ServiceError):
    pass

class ProductNotFoundError(ServiceError):
    pass

class OrderNotFoundError(ServiceError):
    pass

class InvalidQuantityError(ServiceError):
    pass

class UserAlreadyExistsError(ServiceError):
    pass

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Не удалось подтвердить учётные данные",
    headers={"WWW-Authenticate": "Bearer"},
        )

bad_request_exception = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким именем уже существует"
        )

unauthorized_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль",
            headers={"WWW-Authenticate": "Bearer"}
        )