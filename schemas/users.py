from pydantic import BaseModel

class SchemaUser(BaseModel):
    name: str
    phone: str
    address: str