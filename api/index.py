from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud
from .database import SessionLocal, engine
from .schemas import Datasout
from typing import List

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api")
async def root():
    return {"message": "Hello World"}

@app.get("/api/test")
async def test():
    return {"message": "Hello Test"}


@app.get("/api/list", response_model=List[Datasout])
async def read_list(db: Session = Depends(get_db)):
        result = crud.all_list(db)
        return result
