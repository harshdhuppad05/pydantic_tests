from typing import List, Optional

from pydantic import BaseModel

class Address(BaseModel):
    flat_no: int
    street: str
    city: str

class User(BaseModel):
     name: str
     age : int
     Address : Address

class Comment(BaseModel):
    id: int
    comment: str
    replies: Optional[List['Comment']] = None
    # forward refrencing

Comment.model_rebuild()


