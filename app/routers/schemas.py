from pydantic import BaseModel

class comments(BaseModel):
    name: str 
    email: str
    subject: str
    message: str