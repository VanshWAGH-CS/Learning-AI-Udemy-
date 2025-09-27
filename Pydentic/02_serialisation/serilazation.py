from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = Field(default_factory=list)

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }

user = User(
    id=1,
    name="Vansh",
    email="vansh@.ai",
    createdAt=datetime(2024, 3, 15, 13, 30),
    address=Address(
        street="Something",
        city="Nagpur",
        zip_code="009988"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

python_dict = user.dict()       # ✅ use dict()
print(user)
print("="*30)
print(python_dict)

json_str = user.json()          # ✅ use json()
print("="*30)
print(json_str)
