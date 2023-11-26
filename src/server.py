from contextlib import asynccontextmanager
from fastapi import FastAPI
from config.database import create_db_and_tables

# import das novas rotas
from routes.provas_router import provas_router
from routes.resultados_router import resultados_router
from routes.prova_id import provas_router_id
from routes.resultados_provas_id import resultados_router_id
from routes.prova_aplicada_id import provas_aplicadas_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

# Inclusão de novas rotas
app.include_router(provas_router)
app.include_router(resultados_router)
app.include_router(provas_router_id)
app.include_router(provas_aplicadas_router)
app.include_router(resultados_router_id)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}
