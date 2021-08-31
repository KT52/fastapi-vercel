from sqlalchemy.orm import Session
from . import model


def all_list(db: Session):
    return db.query(model.Book).all()
