from pydantic import BaseModel, conint, constr

class UserBase(BaseModel):
    nombre: constr(strip_whitespace=True, min_length=1, max_length=30)
    apellido: constr(strip_whitespace=True, min_length=1, max_length=30)
    direccion: constr(strip_whitespace=True, min_length=1, max_length=50)
    telefono: constr(strip_whitespace=True, min_length=10, max_length=15)
    edad: conint(ge=0, le=120)

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
