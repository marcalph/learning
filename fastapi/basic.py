# done so far
# path prm
# query prm
# request body (send data from client to API)
# query prm and string val
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str|None = None
    price: float
    tax: float|None = None

myapp = FastAPI()

@myapp.get("/")
async def root():
    return {"message": "Hello world"}

@myapp.post("/items/{item_id}") # item_id path prm
async def create_item(item_id: int, item: Item, q: str|None=None): # item req body, q query prm
    result = {"item_id":item_id, **item.dict()}
    if q:
        result.update({"q": q})
    print(f"creating item {item.name.upper()}")
    return result

# path parameters e.g. item_id
@myapp.get("/items/{item_id}")
async def get_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}

############################################################
# if not placed before query would go to endpoint /user/"me"
@myapp.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@myapp.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
############################################################

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


def list_models():
    for name in ModelName:
        print(name)

# path parameter
@myapp.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    list_models()
    match model_name:
        case ModelName.alexnet:
            return {"model_name": model_name, "message": "Deep Learning FTW!"}
        case "lenet":
            return {"model_name": model_name, "message": "LeCNN all the images"}
        case "resnet":
            return {"model_name": model_name, "message": "Have some residuals"}
        case _:
            pass


@myapp.get("/models/path/{file_path:path}")
async def print_output_path(file_path: str):
    print(file_path)
    return None




@myapp.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
from fastapi import Query

# no defaut to query prm makes it needed
@myapp.get("/items-list/")
async def read_item(unneeded_query_prm: str | None = None, 
                    skip: str = Query(default="1", max_length=50), 
                    limit: int = 10
):
    skip=int(skip)
    if unneeded_query_prm:
        return {"skipped": skip, "q": needed_query_prm}
    return fake_items_db[skip : skip + limit]
