from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from services.user_service import UserService
from dependencies import get_user_service

class UserCreateInput(BaseModel):
    user_name: str

class UpdateUserInput(BaseModel):
    user_name: str


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(
    user_data: UserCreateInput,
    user_service: UserService = Depends(get_user_service)
    ):
    try:
        await user_service.add_user(user_name=user_data.user_name)
        return {"status": "success", "message": "User has been successfully added"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@router.get("/")
async def get_users(
    user_service: UserService = Depends(get_user_service)
    ):
    try:
        return await user_service.get_users()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@router.get("/{user_id}")
async def get_users(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
    ):
    try:
        return await user_service.get_user(user_id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@router.put("/{user_id}")
async def change_user_name(
    user_id: int,
    payload: UpdateUserInput,
    user_service: UserService = Depends(get_user_service)
    ):
    try:
        await user_service.update_user(user_id=user_id, user_name=payload.user_name)
        return {"status": "success", "message": "User has been successfully updated"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.delete("/{user_id}")
async def remove_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
    ):
    try:
        await user_service.delete_user(user_id=user_id)
        return {"status": "success", "message": "User and user's orders has been successfully deleted"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))