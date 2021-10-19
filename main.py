from fastapi import FastAPI, UploadFile, File
import uuid
import os
from fastapi.datastructures import Default
from fastapi.responses import Response
from starlette.responses import FileResponse
from typing import List
import uvicorn
from fastapi.responses import FileResponse


app = FastAPI(title="test update image", openapi_url="/api/openapi.json", docs_url="/api/docs", redoc_url="/api/redoc")

db = "./store/"

# add mutiple image
@app.post("/image")
async def creat_image(
    files: List[UploadFile] = File(...)
):
    for file in files:
        file.name = f"{uuid.uuid4()}.jpg"
        data = await file.read()
        with open(f"{db}{file.name}", "wb") as f:
            f.write(data)
        return 'pass'

# return image
@app.get("/home")
async def show_image(file_name):
    return FileResponse("{store}/{file_name}".format(store=db, file_name=file_name))


# ++++++++++++++++++++++++++++++++++++++++++++++ RUN SERVICE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0',port=80, debug=True)
