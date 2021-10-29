from fastapi import Depends, APIRouter, HTTPException
from db.user_db import get_user
from models.user_models import UserIn, UserOut
from fastapi import HTTPException

router = APIRouter()

@router.get("/user/info/{username}")
async def get_name(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out