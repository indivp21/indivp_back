from fastapi import Depends, APIRouter, HTTPException
from db.gerencia_db import get_gerencia
from models.gerencia_models import GerIn, GerOut
from fastapi import HTTPException

router = APIRouter()

@router.get("/Gerencia/{gerencia}")
async def get_dgeren(gerencia: str):
    ger_in_db = get_gerencia(gerencia)
    if ger_in_db == None:
        raise HTTPException(status_code=404, detail="La gerencia no existe")
    ger_out = GerOut(**ger_in_db.dict())
    return ger_out