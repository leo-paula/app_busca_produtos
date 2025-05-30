from fastapi import HTTPException

def getProductAmazon(query):
    try:
        return 'teste'
    except Exception as e:
        raise HTTPException(status_code= 400, detail= 'Ação Inválida')
