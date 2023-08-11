from flask.views import MethodView
from flask import Blueprint, request


categories_blueprint=Blueprint("categories_blueprint", __name__, url_prefix="/api/")


class AllCategories(MethodView):
    def get(self):
        return [{"Mensaje": "Categories"}]


class AddCategories(MethodView):
    def post(self):
        new_category = request.get_json()
        cat=new_category.get("ct")

        if cat is None:
            return{"massage":"No ha ingresado la categoria correcta"},400

        return {"message":"Categoria agregada correctamente :D"}
    

class Categories(MethodView):
    def get(self):
        data=request.get.json()
        id=data.get("id")
        if id is None:
            return{"message": "Categoria inexistente"}, 400
        return{id}


categories_blueprint.add_url_rule(
    "Allcategories",
    view_func=AllCategories.as_view("categories_list")
)


categories_blueprint.add_url_rule(
    "Addcategories",
    view_func=AddCategories.as_view("categories_add")
)


categories_blueprint.add_url_rule(
    "categories",
    view_func=Categories.as_view("id")
)
