from fastapi import FastAPI, applications
from fastapi import HTTPException
from fastapi.exceptions import FastAPIError
from fastapi.middleware.cors import CORSMiddleware
from routers.indicadora_router import router as router_indicadora
from routers.indicadorb_router import router as router_indicadorb
from routers.indicadorc_router import router as router_indicadorc
from routers.indicadord_router import router as router_indicadord
from routers.user_router import router as router_user
from routers.gerencia_router import router as router_gerencia

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","https://indivp.herokuapp.com","https://indivptest.herokuapp.com",
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

api.include_router(router_user)
api.include_router(router_indicadora)
api.include_router(router_indicadorb)
api.include_router(router_indicadorc)
api.include_router(router_indicadord)
api.include_router(router_gerencia)
