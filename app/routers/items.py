from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(tags=["Items"])


# ✅ Get item by ID
@router.get("/get-item/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return item


# ✅ Get items by name (or all items)
@router.get("/get-by-name", response_model=list[schemas.ItemResponse])
def get_items_by_name(name: str | None = Query(None), db: Session = Depends(get_db)):
    items = crud.get_items(db, name)
    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No items found"
        )
    return items


# ✅ Create item (auto-assign ID)
@router.post(
    "/create-item",
    response_model=schemas.ItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


# ✅ Update item by ID (partial updates allowed)
@router.put("/update-item/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.UpdateItem, db: Session = Depends(get_db)):
    updated_item = crud.update_item(db, item_id, item)
    if not updated_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return updated_item


# ✅ Delete item by ID
@router.delete("/delete-item/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    success = crud.delete_item(db, item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return {"detail": "Item deleted successfully"}
