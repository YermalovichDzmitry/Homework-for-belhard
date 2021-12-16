from pydantic import BaseModel
from typing import Any, List

data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {
            'age': 3,
            'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
}


class Data(BaseModel):
    age: int
    name: str
    children: List
    married: bool
    city: Any


print(data)
d = Data(**data)
print(d.json())
