from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def get_items():
    return [{"id": 1, "item": "Laptop"}, {"id": 2, "item": "Phone"}]

@router.post("/items")
def create_item(item: dict):
    return {"message": "Item created", "item": item}