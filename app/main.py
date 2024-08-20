import logging
import sys
from fastapi import FastAPI, Request
from db.conn import cria_banco
from routes import auth_routes, user_routes
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from services.token_service import TokenService


logging.basicConfig(filename='app.log', level=logging.ERROR)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    sys.stderr = open('app.log', 'a')
    logging.exception(
        f"\n{'='*64}\n{'='*64}\n{'Erro'.center(64)}\n{'='*64}\n{'='*64}")
    # logging.exception(f"Unhandled exception: {exc}")
    sys.stderr.close()
    return JSONResponse(
        status_code=500,
        content={"message": "Erro interno do Servidor"}
    )


# middleware para autentificação
@app.middleware("http")
async def autentifica(request: Request, call_next):
    if not request.url.path.startswith("/auth"):
        token = request.headers.get("Authentication")

        if token is None:
            return JSONResponse({"error": "token não encontrado"}, status_code=401)

        dados_token = TokenService.pega_dados_token(token)
        if not dados_token or dados_token['type'] != 'acess':
            return JSONResponse({"error": "token inválido"}, status_code=401)

    return await call_next(request)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(user_routes.router, prefix="/user")


cria_banco()
