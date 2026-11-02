from fastapi import APIRouter, Depends, Query
from typing import List
from schemas import UserCreateInput, UpdateUserInput, UserOut
from services.user_service import UserService
from dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(
    user_data: UserCreateInput,
    user_service: UserService = Depends(get_user_service)
    ) -> dict[str, str]:
    await user_service.add_user(user_name=user_data.user_name)
    return {"status": "success", "message": "User has been successfully added"}

@router.get("/", response_model=List[UserOut])
async def get_users(
    user_service: UserService = Depends(get_user_service),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=1000),
) -> List[UserOut]:
    users = await user_service.get_users(skip=skip, limit=limit)
    return [UserOut(id=u.id, name=u.name) for u in users]

@router.get("/{user_id}", response_model=UserOut)
async def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
    ) -> UserOut:
    user = await user_service.get_user(user_id)
    return UserOut(id=user.id, name=user.name)

@router.put("/{user_id}")
async def change_user_name(
    user_id: int,
    payload: UpdateUserInput,
    user_service: UserService = Depends(get_user_service)
    ) -> dict[str, str]:
    await user_service.update_user(user_id=user_id, user_name=payload.user_name)
    return {"status": "success", "message": "User has been successfully updated"}

@router.delete("/{user_id}")
async def remove_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
    ) -> dict[str, str]:
    await user_service.delete_user(user_id=user_id)
    return {"status": "success", "message": "User and user's orders has been successfully deleted"}