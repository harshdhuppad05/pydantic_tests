print("hello")

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    is_online: bool = False

item = Item(id = 1,name = "chawal",price =  100)
print(item)