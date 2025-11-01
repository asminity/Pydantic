from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    Product_id: int
    items: List[str]
    Quantity: Dict[str, int]
    Coupons: Optional[List[str]] = None
    
User1 = Cart(
    Product_id = 1,
    items = ["Aloo", "Tamatar", "Bhindi"],
    Quantity = {"Aloo": 12, "Tamatar": 6, "Bhindi": 21}
)