from pydantic import BaseModel

class ExampleEvent(BaseModel):
    message: str