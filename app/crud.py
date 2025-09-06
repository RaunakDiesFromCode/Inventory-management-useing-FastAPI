from sqlalchemy.orm import Session
from . import models, schemas


def get_item(db: Session, item_id: int):
    return db.query(models.ItemDB).filter(models.ItemDB.id == item_id).first()


def get_items(db: Session, name: str = None):
    query = db.query(models.ItemDB)
    if name:
        query = query.filter(models.ItemDB.name == name)
    return query.all()


def create_item(db: Session, item_id: int, item: schemas.Item):
    db_item = models.ItemDB(id=item_id, **item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item: schemas.UpdateItem):
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return True
