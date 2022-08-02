from sqlalchemy.orm import Session

import to_do.items.models as models
import to_do.items.schemas as schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item: schemas.Item):
    item_obj = get_item(db, item_id)
    if item_obj is not None:
        item_obj.note = item.note
        db.commit()
        db.refresh(item_obj)
    return item_obj


def delete_item(db: Session, item_id: int):
    item_obj = get_item(db, item_id)
    if item_obj is not None:
        db.delete(item_obj)
        db.commit()
    return {"ok": True}
