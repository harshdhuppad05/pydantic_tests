# seriliazation

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name : str
    email: str
    is_active: bool = True
    created_at: datetime
    addresses: Address

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S'),
        }
    )

user = User(id=1, name="John", email="john.mclean@examplepetstore.com",is_active=False, created_at=datetime(2024, 3, 15, 14, 30), addresses=Address(street="123 Main St", city="New York", zip_code="10001"))
#  using model_dump()

print(user.model_dump())

#  using model_dump_json()
print(user.model_dump_json(indent=4))

