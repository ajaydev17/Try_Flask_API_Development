from . import inventory_product_line_api_blueprint
from ..schema import ProductLineInsertSchema
from apifairy import body, response
from ..models import ProductLine
from .. import database

product_line_insert_schema = ProductLineInsertSchema()


@inventory_product_line_api_blueprint.route('/product-line', methods=['POST'])
@body(product_line_insert_schema)
@response(product_line_insert_schema)
def insert_product_line(kwargs):
    new_product_line = ProductLine(**kwargs)
    database.session.add(new_product_line)
    database.session.commit()
    return new_product_line
