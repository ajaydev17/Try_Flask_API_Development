from . import inventory_attribute_api_blueprint
from ..schema import AttributeInsertSchema
from apifairy import body, response
from ..models import Attribute
from .. import database

attribute_insert_schema = AttributeInsertSchema()


@inventory_attribute_api_blueprint.route('/attribute', methods=['POST'])
@body(attribute_insert_schema)
@response(attribute_insert_schema)
def insert_product(kwargs):
    new_attribute = Attribute(**kwargs)
    database.session.add(new_attribute)
    database.session.commit()
    return new_attribute

