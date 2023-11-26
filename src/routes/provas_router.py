from fastapi import APIRouter, HTTPException
from models.provas_model import Provas
from config.database import get_session

provas_router = APIRouter(prefix="/provas")

@provas_router.post("")
def cria_prova(prova: Provas):
    with get_session() as session:
        existing_prova = session.query(Provas).filter(
            Provas.descricao == prova.descricao,
            Provas.data_prova == prova.data_prova
        ).first()

        if existing_prova:
            raise HTTPException(status_code=400, detail="Prova já cadastrada.")
    
        session.add(prova)
        session.commit()
        session.refresh(prova)
        return prova