from . import inventory_product_line_api_blueprint
from ..schema import ProductLineInsertSchema
from apifairy import body, response
from ..models import ProductLine, AttributeValue
from .. import database

product_line_insert_schema = ProductLineInsertSchema()


@inventory_product_line_api_blueprint.route('/product-line', methods=['POST'])
@body(product_line_insert_schema)
@response(product_line_insert_schema)
def insert_product_line(product_line_data):
    product_attribute_ids = product_line_data.pop('product_attribute_ids', [])
    new_product_line = ProductLine(**product_line_data)
    new_product_line.product_attributes = AttributeValue.query.filter(
        AttributeValue.id.in_(product_attribute_ids)
    ).all()
    database.session.add(new_product_line)
    database.session.commit()
    return new_product_line
