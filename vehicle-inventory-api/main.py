import uvicorn
from fastapi import FastAPI
from routes import vehicle_route

app = FastAPI()
Host = "127.0.0.1"
PORT = 5005


app.include_router(vehicle_route.router, prefix="/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host=Host, port=PORT, reload=True)