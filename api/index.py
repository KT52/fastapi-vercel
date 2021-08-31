from fastapi import FastAPI

app=FastAPI()

@app.get("/api")
async def root():
    return {"message": "Hello World"}

@app.get("/api/test")
async def test():
    return {"message": "Hello Test"}