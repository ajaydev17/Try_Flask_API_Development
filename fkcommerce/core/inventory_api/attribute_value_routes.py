from . import inventory_attribute_value_api_blueprint
from ..schema import AttributeValueInsertSchema
from apifairy import body, response
from ..models import AttributeValue
from .. import database

attribute_value_insert_schema = AttributeValueInsertSchema()


@inventory_attribute_value_api_blueprint.route('/attribute-value', methods=['POST'])
@body(attribute_value_insert_schema)
@response(attribute_value_insert_schema)
def insert_product(kwargs):
    new_attribute_value = AttributeValue(**kwargs)
    database.session.add(new_attribute_value)
    database.session.commit()
    return new_attribute_value

