#!/usr/bin/python3
from app import db  # Assuming you have SQLAlchemy set up

from app.models.user import User

class SQLAlchemyRepository:
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()

class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, email):
        """Fetch a user by their email address."""
        return self.model.query.filter_by(email=email).first()

    def get_user_by_username(self, username):
        """Fetch a user by their username."""
        return self.model.query.filter_by(username=username).first()
