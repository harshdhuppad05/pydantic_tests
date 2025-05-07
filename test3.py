from pydantic import BaseModel, Field

class Item(BaseModel):
    id : int
    name: str = Field(...,ge=3, example="Foo")
    description: str = Field(None,min_length=3, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: float = Field(None, example=3.2)

