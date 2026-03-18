from pydantic import BaseModel, ValidationError


class DataModel(BaseModel):
    number: int


class Response[DataT](BaseModel):  
    data: DataT  


print(Response[int](data=1))

print(Response[str](data='value'))

print(Response[str](data='value').model_dump())

data = DataModel(number=1)

print(Response[DataModel](data=data).model_dump())

try:
    Response[int](data='value')
except ValidationError as e:
    print(e)
    