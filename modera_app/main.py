import uvicorn
from fastapi import FastAPI
from modera_app.routes import api, auth

app = FastAPI()


app.include_router(api.router, prefix="/api", tags=['users'])
app.include_router(auth.router, prefix="/auth", tags=['auth'])


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)