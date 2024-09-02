from flask import Blueprint

inventory_category_api_blueprint = Blueprint('inventory_category_api', __name__)
inventory_product_api_blueprint = Blueprint('inventory_product_api', __name__)
inventory_product_line_api_blueprint = Blueprint('inventory_product_line_api', __name__)
inventory_product_image_api_blueprint = Blueprint('inventory_product_line_image_api', __name__)
inventory_attribute_api_blueprint = Blueprint('inventory_attribute_api_blueprint', __name__)
inventory_seasonal_event_api_blueprint = Blueprint('inventory_seasonal_event_api_blueprint', __name__)

from . import category_routes, product_routes, product_line_routes, product_image_routes  # noqa: F401
