from fastapi import FastAPI, UploadFile, File, responses
import uuid
import os
from fastapi.responses import Response


app = FastAPI(app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/openapi.json", docs_url="/api/docs", redoc_url="/api/redoc"))

db = []

@app.post("/image")
async def creat_image(file: UploadFile = File()):
    file.name = f"{uuid.uuid4()}.jpg"
    data = await file.read()
    db.append(data)
    return {"filename": file.name}

@app.get("/home")
async def show_image():
    responses = Response(content=db)
    return responses