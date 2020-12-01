import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/api/v1/get_message")
async def get_message():
    return "Hello, world from the server!"

@app.get("/test")
async def test():
    return "hogehogehoge"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

