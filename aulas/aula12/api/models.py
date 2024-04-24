from pydantic import BaseModel


class Eats(BaseModel):
    name: str
    sku: int
    price: str
    enabled: bool
    id: str


