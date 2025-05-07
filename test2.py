from pydantic import BaseModel
from typing import List, Optional, Dict

class Cart(BaseModel):
    id: int
    items: List[str]
    quantities: Dict[str, int]
    image: Optional[str] = None
