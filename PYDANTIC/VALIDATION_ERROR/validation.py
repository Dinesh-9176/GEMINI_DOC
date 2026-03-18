from pydantic import BaseModel, ValidationError
import logging

logging.basicConfig(level=logging.ERROR)

class item(BaseModel):
    name :str
    price : float
    available :int

try:
    i=item(name="dinesh", price="free", available="yes")
    print(i)
except ValidationError as e:
    logging.error(e)