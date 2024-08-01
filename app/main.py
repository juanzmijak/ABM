from fastapi import FastAPI, Depends, HTTPException
from . import schemas, crud, auth
from .audit import log_event

app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, api_key: str = Depends(auth.get_api_key)):
    user_id = crud.create_user(user=user)
    log_event(f"User created: {user.nombre} {user.apellido}")
    return crud.get_user(user_id)

@app.get("/users/", response_model=list[schemas.User])
def read_users(nombre: str, api_key: str = Depends(auth.get_api_key)):
    users = crud.get_user_by_name(nombre)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, api_key: str = Depends(auth.get_api_key)):
    user = crud.get_user(user_id)
    return user

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, api_key: str = Depends(auth.get_api_key)):
    updated_user = crud.update_user(user_id, user)
    log_event(f"User updated: {user_id}")
    return updated_user

##@app.delete("/users/{user_id}", response_model=schemas.User)
@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, api_key: str = Depends(auth.get_api_key)):
    crud.delete_user(user_id)
    log_event(f"User deleted: {user_id}")
    return {"detail": "User deleted"}
