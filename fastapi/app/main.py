from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.get("/health")
def health() -> dict:
    return {"statusCode": 200, "message": "OK"}