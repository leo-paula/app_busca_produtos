from fastapi import FastAPI
from App.Routes import router

app = FastAPI()
app.include_router(router)
