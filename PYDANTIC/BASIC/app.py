from pydantic import BaseModel

class user(BaseModel):
    name : str
    age : int
    email : str

u = user(name="dinesh",age="21",email="dkgmail.com")
print(u)


