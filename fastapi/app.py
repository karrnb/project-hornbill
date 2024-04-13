from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.recipes import RecipeHandler


TODOS = [{
    "id": "1",
    "item": "Test TODO item 1"
}, {
    "id": "2",
    "item": "Test TODO item 2"
}]

app = FastAPI()

origins = [
    "http://localhost:9000",
    "localhost:9000",
    "http://localhost:8000",
    "localhost:8000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}

@app.get("/test-todo", tags=["todo"])
async def get_todos() -> dict:
    return {"data": TODOS}

@app.get("/get-recipes", tags=["all"])
async def read_all() -> dict:
    """TODO"""

    rh = RecipeHandler()

    return rh.get_all_recipes()

@app.post("/create-recipe", tags=["recipe", "create"])
async def create_recipe() -> dict:
    """TODO"""

    rh = RecipeHandler()

    pass

@app.post("/update-recipe", tags=["recipe", "update"])
async def update_recipe() -> dict:
    """TODO"""

    rh = RecipeHandler()

    pass

@app.post("/delete-recipe", tags=["recipe", "delete"])
async def delete_recipe() -> dict:
    """TODO"""

    rh = RecipeHandler()
    
    pass
