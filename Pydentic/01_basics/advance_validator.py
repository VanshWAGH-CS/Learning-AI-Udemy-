from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

# Multiple field validation example
class Person(BaseModel):
    first_name: str
    last_name: str

    # Validator to ensure both first_name and last_name are capitalized
    @field_validator('first_name', 'last_name')
    def names_must_be_capitalize(cls, v):
        if not v.istitle():
            raise ValueError("Names must be capitalised")
        return v

class User(BaseModel):
    email: str

    # Validator to normalize email by converting to lowercase and stripping spaces
    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()

class Product(BaseModel):
    price: str  # Example: "$4.44"

    # Validator to parse price string to float before assignment
    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', '').replace(',', ''))
        return v  # In case it's already a float

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    # Model-level validator to ensure end_date is after start_date
    @model_validator(mode="after")
    def validate_date_range(self):
        if self.end_date <= self.start_date:
            raise ValueError('end date must be after start date')
        return self