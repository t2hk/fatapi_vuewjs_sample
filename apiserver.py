import uvicorn
import requests
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()

minio_service_url = "http://t2-minio-sv.localdev:9000/minio/webrpc"
minio_user = "foobar"
minio_password = "hogehoge"

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/api/v1/get_message")
async def get_message():
    return "Hello, world from the server!"

@app.get("/api/v1/get_minio_token")
async def get_minio_token():
    headers = {
      "Content-Type": "application/json",
      "User-Agent": "Mozilla/5.0"
    }
    data = '{"id":1,"jsonrpc":"2.0","params":{"username":"%s","password":"%s"},"method":"web.Login"}' % (minio_user, minio_password)
    response = requests.post(minio_service_url, headers=headers, data=data)#, verify=False)

    token = response.json()["result"]["token"]
    return token

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

