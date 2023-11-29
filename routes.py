from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import User 

router = APIRouter()

# POST/BOOK

@router.post("/user", response_description="Create a new User", status_code=status.HTTP_201_CREATED, response_model=User)
def create_book(request: Request, User: User = Body(...)):
    user = jsonable_encoder(User)
    new_book = request.app.database["user"].insert_one(user)
    created_book = request.app.database["user"].find_one(
        {"_id": new_book.inserted_id}
    )

    return created_book
