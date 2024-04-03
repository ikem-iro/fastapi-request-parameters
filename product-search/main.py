import uvicorn
from fastapi import FastAPI
from routes import product_route




app = FastAPI()

PORT = 5000

Host = "127.0.0.1"

app.include_router(product_route.router, prefix='/v1')



if __name__ == "__main__":
    uvicorn.run("main:app", host=Host, port= PORT, reload=True)