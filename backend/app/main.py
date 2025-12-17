from fastapi import FastAPI

app = FastAPI(title="LinkedIn Clone API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the LinkedIn Clone API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
