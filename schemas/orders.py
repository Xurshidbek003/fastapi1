from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class SchemaItems(BaseModel):
    book_id: int = Field(gt=0)
    quantity: int = Field(gt=0)


class SchemaOrder(BaseModel):
    user_id: int = Field(gt=0)
    order_date: datetime
    items: List[SchemaItems]