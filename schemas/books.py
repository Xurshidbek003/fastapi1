from pydantic import BaseModel, Field


class SchemaBook(BaseModel):
    name: str
    author: str
    price: int = Field(gt=0)
    amount: int = Field(ge=0)