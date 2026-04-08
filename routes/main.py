from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Besties Cleaning backend is live"}


@app.get("/health")
def health():
    return {"status": "ok"}
