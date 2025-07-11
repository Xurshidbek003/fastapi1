from datetime import date
from pydantic import BaseModel

class SchemaUser(BaseModel):
    full_name: str
    username: str
    password: str
    birth_date: date