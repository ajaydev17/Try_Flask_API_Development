from . import inventory_product_type_api_blueprint
from ..schema import ProductTypeInsertSchema
from apifairy import body, response
from ..models import ProductType
from .. import database

product_type_insert_schema = ProductTypeInsertSchema()


@inventory_product_type_api_blueprint.route('/product-type', methods=['POST'])
@body(product_type_insert_schema)
@response(product_type_insert_schema)
def insert_product(kwargs):
    new_product_type = ProductType(**kwargs)
    database.session.add(new_product_type)
    database.session.commit()
    return new_product_type

