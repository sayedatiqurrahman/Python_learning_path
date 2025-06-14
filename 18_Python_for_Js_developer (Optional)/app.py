from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
def home():
    return {"data": "Welcome to Home", "status": 200}


@app.get("/about")
def about():
    return {"data": "Welcome to About us", "status": 200}


@app.post("/upload")
def handleImage(files: list[UploadFile]):
    print(files)
    return {"status": 200, "message": "Got the file"}


import uvicorn

uvicorn.run(app)
