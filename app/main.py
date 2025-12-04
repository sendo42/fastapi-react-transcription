from fastapi import FastAPI, File, UploadFile
import uvicorn
##from uvicorn_config import config
from fastapi.responses import HTMLResponse, RedirectResponse
from pathlib import Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World" : "Hello World"}

@app.get("/hello", response_class=HTMLResponse)
def html():
    return "hello "


UPLOAD_DIR = Path("./input")

@app.post("/uploadAudio")
async def uploadAudio(file: UploadFile = File(...)):
    print("成功")
    return {"filename" : file.filename}
