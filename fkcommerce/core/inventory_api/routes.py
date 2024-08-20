from . import inventory_category_api_blueprint
from ..schema import CategorySchema
from apifairy import response
from ..models import Category

category_schema = CategorySchema(many=True)


@inventory_category_api_blueprint.route('/category', methods=['GET'])
@response(category_schema)
def category():
    return Category.query.all()
