from python_cms.db import BaseModel, db
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship

class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(80), nullable=False)

    posts = db.relationship('PostModel', back_populates='category')

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get(cls, id):
        return cls.query.get(id)