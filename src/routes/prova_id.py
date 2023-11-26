from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlmodel import select
from src.config.database import get_session
from src.models.provas_model import Provas
from src.models.resultados_model import Resultados

provas_router = APIRouter(prefix="/provas")

@provas_router.delete("/{id}")
def deleta_prova(id: int):
    with get_session() as session:
        statement = select(Resultados).where(Resultados.prova_id == id)
        resultados = session.exec(statement).all()

        if resultados:
            raise HTTPException(status_code=400, detail="Não é possível excluir a prova, pois existem resultados de provas cadastrados.")

        prova = session.get(Provas, id)
        if not prova:
            raise HTTPException(status_code=404, detail="Prova não encontrada")

        session.delete(prova)
        session.commit()

        return {"message": "Prova excluída com sucesso"}
