from flask.views import MethodView
from flask import Blueprint, request
from .models import Users

users_blueprint=Blueprint("Users_blueprint", __name__, url_prefix="/api/")


class UsersList(MethodView):
    def get(self):
        
        return [{"name": "Jose"}, {"name": "Ricardo"}]


class UsersResources(MethodView):
    def post(self):
        data = request.get_json()

        email = data.get("email")
        username= data.get("username")
        if email is None:
            return {"message": "No as ingresado tu correo"}, 400
        if username is None:
            return {"message":"No has ingresado tu username"}, 400
        
        return {"message":"Bienvenido :D"}
    
        
users_blueprint.add_url_rule(
    "users",
    view_func=UsersList.as_view("users_list")
)

        
users_blueprint.add_url_rule(
    "users",
    view_func=UsersResources.as_view("users_resources")
)

