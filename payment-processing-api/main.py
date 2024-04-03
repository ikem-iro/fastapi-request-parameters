import uvicorn
from fastapi import FastAPI
from routes import payment_route


app = FastAPI()

Host = "127.0.0.1"

PORT = 5004

app.include_router(payment_route.router, prefix="/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host=Host, port=PORT, reload=True)