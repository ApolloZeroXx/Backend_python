from flask.views import MethodView
from flask import Blueprint
from .models import Roles

roles_blueprint=Blueprint("roles_blueprint", __name__, url_prefix="/api/")


class RolesList(MethodView):
    def get(self):
        
        return [{"name": "Admin"}, {"name": "User"}]

roles_blueprint.add_url_rule(
    "roles",
    view_func=RolesList.as_view("roles_list")
)
