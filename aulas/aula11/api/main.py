from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

products = {
    1: {
        "name": "banana",
        "preço": 0.5,
        "qualidade": "boa"
    }
}

class Product(BaseModel):
    name: str
    preço: int
    qualidade: str

class UpdateProduct(BaseModel):
    name: str
    preço: int
    qualidade: str

@app.get("/")
def index():
    return{"name": "Frist Data"}

@app.get("/get-product/{product_id}")
def get_product(product_id: int = Path( description= "The ID of the product you want to view" , gt= 0 , lt=3)):
    return products[product_id]

@app.post("/create-product/{product_id}")
def create_student(product_id: int , product: Product):
    if product_id in products:
        return{"Error": "Product exists"}

    products[product_id] = product
    return products[product_id]



