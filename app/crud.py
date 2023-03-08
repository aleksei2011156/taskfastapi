from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_history(db: Session, **transact: schemas.HistoryCreate):
    user_id: int = transact['name']
    user: schemas.User = get_user(db, user_id)
    count = transact['count']
    if transact['type'] == 0:
        db_history = models.History(name=transact['name'], type=transact['type'], count=count, status=True)
        user.balance = user.balance + count
    if transact['type'] == 1:
        if user.balance - count >= 0:
            db_history = models.History(name=transact['id'], type=transact['type'], count=count, status=True)
            user.balance = user.balance - count
        else:
            db_history = models.History(name=transact['id'], type=transact['type'], count=count, status=False)
    db.add(db_history)
    db.commit()
    # db.refresh(db_user)
    return


def get_history(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.History).filter(models.History.name == user_id).offset(skip).limit(limit).all()
