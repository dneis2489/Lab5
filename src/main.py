from fastapi import FastAPI
from src.web_app import api_router

app = FastAPI()

# Включаем роутер API
app.include_router(api_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
