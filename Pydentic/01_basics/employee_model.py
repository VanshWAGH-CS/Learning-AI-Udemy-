from typing import Optional
from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Emplyee Name",
        examples="Hitest Choudhary"
    )
    department: Optional[str] = 'Genral'
    salary: float = Field(
        ...,
        ge=10000#greater than equal to
    )


