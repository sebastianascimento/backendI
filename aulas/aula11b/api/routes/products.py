from fastapi import APIRouter
from fake import faker

fake = Faker()





router = APIRouter(prefix="/product" , tags=["Product"])

@router.get("")
def get_all_product():

    total_rows=20

    result = [
        Product(
            id=faker.isbn10()
            name=fake.lorem(nr_words=2),
            price=fake.pricetag(),
            enabled=True,
            sku=100
        )
        for _ in range(total_rows)
    ]