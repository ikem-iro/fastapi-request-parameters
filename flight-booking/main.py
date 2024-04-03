import uvicorn
from fastapi import FastAPI
from routes import booking_route


app = FastAPI()


PORT = 5001




app.include_router(booking_route.router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=PORT, reload=True)