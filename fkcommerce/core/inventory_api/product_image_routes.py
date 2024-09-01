from . import inventory_product_image_api_blueprint
from ..schema import ProductImageInsertSchema
from apifairy import body, response
from ..models import ProductImage
from .. import database

product_image_insert_schema = ProductImageInsertSchema()


@inventory_product_image_api_blueprint.route('/product-image', methods=['POST'])
@body(product_image_insert_schema)
@response(product_image_insert_schema)
def insert_product_line_image(kwargs):
    new_product_image = ProductImage(**kwargs)
    database.session.add(new_product_image)
    database.session.commit()
    return new_product_image
