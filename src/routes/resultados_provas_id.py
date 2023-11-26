from fastapi import APIRouter, HTTPException
from sqlmodel import select
from src.config.database import get_session
from src.models.provas_model import Provas
from src.models.resultados_model import Resultados

resultados_router = APIRouter(prefix="/resultados_provas")

@resultados_router.get("/{prova_id}")
def get_resultados_prova(prova_id: int):
    with get_session() as session:
        prova = session.get(Provas, prova_id)

        if not prova:
            raise HTTPException(status_code=404, detail="Prova não encontrada")

        statement = select(Resultados).where(Resultados.prova_id == prova_id)
        resultados = session.exec(statement).all()

        dados_resultados = []
        for resultado in resultados:
            resultado_final = "aprovado" if resultado.nota >= 7 else "recuperação" if 5 <= resultado.nota < 7 else "reprovado"
            dados_aluno = {
                "nome": resultado.nome,
                "nota": resultado.nota,
                "resultado_final": resultado_final
            }
            dados_resultados.append(dados_aluno)

        dados_prova = {
            "descricao": prova.descricao,
            "data_prova": prova.data_prova,
            "resultados_alunos": dados_resultados
        }

        return dados_prova
