from . import inventory_product_api_blueprint
from ..schema import ProductInsertSchema
from apifairy import body, response
from ..models import Product, ProductType
from .. import database

product_insert_schema = ProductInsertSchema()


@inventory_product_api_blueprint.route('/product', methods=['POST'])
@body(product_insert_schema)
@response(product_insert_schema)
def insert_product(product_data):
    product_type_ids = product_data.pop('product_type_ids', [])
    new_product = Product(**product_data)
    new_product.product_types = ProductType.query.filter(
        ProductType.id.in_(product_type_ids)
    ).all()
    database.session.add(new_product)
    database.session.commit()
    return new_product
