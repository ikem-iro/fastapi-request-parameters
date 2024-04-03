import uvicorn
from fastapi import FastAPI
from routes import user_route
from config.file_config import create_file


app = FastAPI()

create_file()

host = "127.0.0.1"
PORT = 5002


app.include_router(user_route.router, prefix='/v1')



if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port= PORT, reload=True)