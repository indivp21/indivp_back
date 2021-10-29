from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class UserInDB(BaseModel):
    username: str
    password: str

database_users = Dict[str, UserInDB]
database_users = {
    "Principal": UserInDB(**{"username":"Admin",
                            "password":"Indicor22"}),
    "Consulta": UserInDB(**{"username":"General",
                            "password":"22032021"})
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None