import logging
from fastapi import FastAPI, Request, Mu
from db.conn import cria_banco
from routes import auth_routes
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


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
async def global_exception_handler(request : Request, exc: Exception):
    logging.error(f"Unhandled exception: {exc.with_traceback}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"}
    )



#rotas do fastapi
app.include_router(auth_routes.router)

#middleware para autentificação

@app.middleware
def autentifica(request: Request, call_next):
    pass

cria_banco()