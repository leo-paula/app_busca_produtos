from fastapi import APIRouter, HTTPException, Query
from typing import List
from App.controllers.mercadoLivre import getProductMercadoLivre
from App.controllers.amazon import getProductAmazon
router = APIRouter()

@router.get("/")
async def root():
    try:
        return {"message": 'Base da Api'}
    except Exception as e:
        raise HTTPException(status_code=400, detail='Não foi possível realizar a ação')


@router.get('/mercadolivre/')
async def get_ml_product(query: str = Query(..., description="Consulta para o produto")):
    try:
        result = getProductMercadoLivre(query)
        return {"query": query, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail='Não foi possível realizar a ação')


@router.get('/amazon')
async def get_amz_product(query: str = Query(..., description="Consulta para o produto")):
    try:
        result = getProductAmazon(query)
        return {"query": query, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail='Não foi possível realizar a ação')