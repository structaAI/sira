from fastapi import FastApi
from uvicorn import run

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)