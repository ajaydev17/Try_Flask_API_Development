from . import inventory_category_api_blueprint
from ..schema import CategorySchema
from apifairy import response, body
from ..models import Category
from .. import database

category_schema = CategorySchema(many=True)


@inventory_category_api_blueprint.route('/category', methods=['GET'])
@response(category_schema)
def category():
    return Category.query.all()


@inventory_category_api_blueprint.route('/category', methods=['POST'])
@body(category_schema)
def insert_category(kwargs):
    new_category = Category(**kwargs)
    database.session.add(new_category)
    database.session.commit()
    return
