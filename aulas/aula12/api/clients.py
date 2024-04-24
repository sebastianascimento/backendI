import json
from typing import List

def get_eats(db:str)->List[dict]:
    result = []
    with open(db , "r") as data:
        result=json.loads("".join(data.readlines()))
    return result


