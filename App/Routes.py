from fastapi import APIRouter, HTTPException, Query
from typing import List
from App.controllers.mercadoLivre import getProductMercadoLivre

router = APIRouter()

@router.get("/")
async def root():
    try:
        return {"message": 'Base da Api'}
    except Exception as e:
        raise HTTPException(status_code=400, detail='Não foi possível realizar a ação')


@router.get('/mercadolivre/')
async def get_ml_product(query: List[str] = Query(..., description="Consulta para o produto")):
    try:
        results = []
        for q in query:
            result = getProductMercadoLivre(q)
            results.append({"query": q, "result": result})
        return {"message": "Pegando produtos Mercado Livre...", "results": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail='Não foi possível realizar a ação')
