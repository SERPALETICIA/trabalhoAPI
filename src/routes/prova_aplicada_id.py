from fastapi import APIRouter, HTTPException
from sqlmodel import select
from src.config.database import get_session
from src.models.provas_model import Provas
from src.models.resultados_model import Resultados

provas_aplicadas_router = APIRouter(prefix="/provas_aplicadas")

@provas_aplicadas_router.patch("/{id}")
def altera_respostas_prova(id: int, resultado: Resultados):
    with get_session() as session:
        resultado_db = session.get(Resultados, id)

        if not resultado_db:
            raise HTTPException(status_code=404, detail="Resultado da prova não encontrado")

        prova = session.get(Provas, resultado_db.prova_id)

        for i in range(1, 11):
            questao = f"q{i}"
            resposta_aluno = getattr(resultado, questao)
            setattr(resultado_db, questao, resposta_aluno)

        nota = 0
        for i in range(1, 11):
            questao = f"q{i}"
            resposta_aluno = getattr(resultado_db, questao)
            resposta_correta = getattr(prova, questao)
            if resposta_aluno == resposta_correta:
                nota += 1

        resultado_db.nota = (nota / 10) * 10

        session.commit()
        session.refresh(resultado_db)

        return resultado_db
