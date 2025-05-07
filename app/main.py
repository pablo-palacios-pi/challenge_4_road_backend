from fastapi import FastAPI
from routers import router
from schemas import inicio_db



app = FastAPI()

inicio_db()

app.include_router(router, prefix="/api_train")