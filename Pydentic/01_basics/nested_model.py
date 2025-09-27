from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str 
    postal_code: str


class User(BaseModel):
    id: int
    name: str 
    address: Address



address = Address(
    street="12335 something",
    city="Nagpur",
    postal_code="10001"
)

user = User(
    id=1,
    name="Vansh",
    address=address
)


user_data = {
    "id":1,
    "name": "Vansh",
    "address":{
        "street": "312",
        "city": "Nagpur",
        "postal_code":"20002"
    }
}

user = User(**user_data)

print(user)