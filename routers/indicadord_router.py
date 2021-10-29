from fastapi import Depends, APIRouter, HTTPException
from db.indicadord_db import get_indicador
from models.indicador_models import IndicadorIn, IndicadorOut
from fastapi import HTTPException

router = APIRouter()

@router.get("/Indicadoresd/{indicador}")
async def get_indicor(indicador: str):
    Indicador_in_db = get_indicador(indicador)
    if Indicador_in_db == None:
        raise HTTPException(status_code=404, detail="El indicador no existe")
    indicador_out = IndicadorOut(**Indicador_in_db.dict())
    return indicador_out