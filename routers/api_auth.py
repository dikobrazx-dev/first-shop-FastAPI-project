from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from exceptions import UserAlreadyExistsError, bad_request_exception, unauthorized_exception
from auth import create_access_token
from dependencies import get_user_service
from services.user_service import UserService
from schemas import UserCreateInput, UserOut

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreateInput,
    user_service: UserService = Depends(get_user_service)
):
    try:
        db_user = await user_service.register_user(user_data.user_name, user_data.password)
    except UserAlreadyExistsError:
        raise bad_request_exception
    return UserOut(id=db_user.id, name=db_user.name)


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: UserService = Depends(get_user_service)
):
    user = await user_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise unauthorized_exception
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}