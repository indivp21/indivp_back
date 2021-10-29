from pydantic import BaseModel

class GerIn(BaseModel):
    name: str
    indigen: float
    rango: str

class GerOut(BaseModel):
    name: str
    indigen: float
    rango: str