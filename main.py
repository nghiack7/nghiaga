from fastapi import FastAPI, UploadFile, File
import uuid
import os
from fastapi.datastructures import Default
from fastapi.responses import Response


app = FastAPI(title="test update image", openapi_url="/api/openapi.json", docs_url="/api/docs", redoc_url="/api/redoc")

db = "Store/"

@app.post("/image")
async def creat_image(file: UploadFile = File(...)):
    file.name = f"{uuid.uuid4()}.jpg"
    data = await file.read()
    with open(f"{db}{file.name}", "wb") as f:
        f.write(data)
    return {"filename": file.name}

@app.get("/home")
async def show_image():
    responses = Response(content=db)
    return responses
