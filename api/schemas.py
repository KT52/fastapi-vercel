from pydantic import BaseModel
from typing import Optional

class Datasout(BaseModel):
    title: str
    author: str
    publisher: Optional[str] = None
    id: int

    class Config:
        orm_mode = True


