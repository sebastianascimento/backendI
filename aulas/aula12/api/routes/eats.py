from typing import List
from fastapi import APIRouter
from faker import Faker
from api.clients import get_eats
from api.models import Eats

fake = Faker()

router= APIRouter(prefix="/eats" , tags=["Eats"])

@router.get("")
def get_all_eats()-> List[Eats]:
   result= [
        Eats(**eats)
        for eats in get_eats(db="/app/db.json")
   ]
   return result

@router.get_name("/name")
def get_name_eats()-> List[Eats]:
   