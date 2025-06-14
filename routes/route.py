from fastapi import APIRouter, HTTPException, status
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# GET all todos
@router.get("/", status_code=200)
async def get_todos():
    todos = list_serial(collection_name.find())
    return {"status": "success", "data": todos}


# POST a new todo
@router.post("/", status_code=201)
async def post_todo(todo: Todo):
    result = collection_name.insert_one(dict(todo))
    if result.inserted_id:
        return {"status": "success", "message": "Todo added successfully."}
    else:
        raise HTTPException(status_code=500, detail="Failed to add todo.")


# PUT update a todo by ID
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    result = collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(todo)}
    )
    if result:
        return {"status": "success", "message": "Todo updated successfully."}
    else:
        raise HTTPException(status_code=404, detail="Todo not found.")


# DELETE a todo by ID
@router.delete("/{id}")
async def delete_todo(id: str):
    result = collection_name.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return {"status": "success", "message": "Todo deleted successfully."}
    else:
        raise HTTPException(status_code=404, detail="Todo not found.")


@router.get("/{id}", status_code=200)
async def get_single_todo(id: str):
    try:
        todo = collection_name.find_one({"_id": ObjectId(id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format.")

    if todo:
        return {"status": "success", "data": todo}
    else:
        raise HTTPException(status_code=404, detail="Todo not found.")
