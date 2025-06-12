import uvicorn
import os
from fastapi import FastAPI
from Routes import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", default=8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )
