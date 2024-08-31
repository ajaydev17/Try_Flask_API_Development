from . import inventory_product_api_blueprint
from ..schema import ProductInsertSchema
from apifairy import body, response
from ..models import Product
from .. import database

product_insert_schema = ProductInsertSchema()


@inventory_product_api_blueprint.route('/product', methods=['POST'])
@body(product_insert_schema)
@response(product_insert_schema)
def insert_product(kwargs):
    new_product = Product(**kwargs)
    database.session.add(new_product)
    database.session.commit()
    return new_product
