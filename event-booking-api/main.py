import uvicorn
from fastapi import FastAPI
from routes import event_booking_route


app = FastAPI()

host = "127.0.0.1"
PORT = 5003


app.include_router(event_booking_route.router, prefix="/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=PORT, reload=True)

