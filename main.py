from typing import List, Dict, Union
import json

import requests
from fastapi import Depends, FastAPI, HTTPException, Response, Request, Body
from sqlalchemy.orm import Session

from app import models, crud, schemas
from app.database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"name": "Aleksei"}


@app.get("/user/{user_id}", response_model=schemas.User)
async def user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users", response_model=List[schemas.User])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post('/transact')
async def transact(request: Request, db: Session = Depends(get_db)):
    info = await request.json()
    crud.create_history(db, **info)
    print(info)
    return {"status": "Ok"}