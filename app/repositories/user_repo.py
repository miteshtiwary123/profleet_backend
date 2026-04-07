from app.models.user import User

def get_user_by_email(db, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db, user_data):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
