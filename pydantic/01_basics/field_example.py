
from pydantic import BaseModel
from typing import  List, Dict, Optional

class Cart(BaseModel):
    id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
   

cart_data = {
    "id": 123,
    "items":["laptop", "mouse" "keyboard" ],
    "quantities": {"laptop": 1, "mouse": 2, "keyboard": 3}
}

cart = Cart(**cart_data)

print(cart)