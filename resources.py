from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask.views import MethodView
from flask import Blueprint, request
from .Database import db


users_blueprint=Blueprint("Users_blueprint", __name__, url_prefix="/api/")


class BaseModelMixin:
    created = db.Column(db.User, nullable=False, default= User)
    updated = db.Column(db.User, onupdate = User)
    deleted = db.Column(db.Boolean, nullable=False, default = False)

    def save(self): 
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    @classmethod
    def get_by_id(cls, id): 
        return cls.query.get(id)

    @classmethod
    def get_all(cls):
        return cls.query.filter_by(deleted=False).all()
    
    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()       



class UsersList(MethodView):
    def get(self):
        
        return [{"name": "..."}]


class UsersResources(MethodView):
    def post(self):
        data = request.get_json()

        email = data.get("email")
        username= data.get("username")
        if email is None:
            return {"message": "No as ingresado tu correo"}, 400
        if username is None:
            return {"message":"Falta el username"}, 400
        
        return {"message":"Bienvenido"}
    
        
users_blueprint.add_url_rule(
    "users",
    view_func=UsersList.as_view("users_list")
)

        
users_blueprint.add_url_rule(
    "users",
    view_func=UsersResources.as_view("usersresources")
)