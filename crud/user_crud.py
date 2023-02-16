from sqlalchemy.orm import Session

from domain.user import CreateUser
from model.user import User
from database import get_db


def get_user_by_id(user_id: int, db: Session = get_db()):
    return db.query(User).filter(User.id == user_id).first()


def create_user(data: CreateUser, db: Session = get_db()):
    user = User(name=data.name, email=data.email, password=data.password,
                is_active=data.is_active)
    db.add(user)
    db.commit()