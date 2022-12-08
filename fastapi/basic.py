# done so far
# path prm
# query prm
# request body (send data from client to API)
# query prm and string validation
# path prm and num validatons
# request body parameters w/ pydantic basemodel (to be passed to the request put/post)
# body fields to enforce validation/metadata inside of pydantic models
# body fields : the field class from pydantic can enforce validation on request body attr
# examples
# extra data type: uuid, datetime/date, frozenset
# cookie parameter, header

from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from fastapi import Query, Path, Body
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
async def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})  # type: ignore
    return results

############################################################
# if not placed before query would go to endpoint /user/"me"
@myapp.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@myapp.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
############################################################




@myapp.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results

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





fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# no defaut to query prm makes it needed
@myapp.get("/items-list/")
async def read_item(unneeded_query_prm: str | None = None, 
                    skip: str = Query(default="1", max_length=50), 
                    limit: int = 10
):
    skip_=int(skip)
    if unneeded_query_prm:
        return {"skipped": skip, "q": unneeded_query_prm}
    return fake_items_db[skip_ : skip_ + limit]
