from flask import Blueprint

inventory_category_api_blueprint = Blueprint('inventory_category_api', __name__)
inventory_product_api_blueprint = Blueprint('inventory_product_api', __name__)

from . import category_routes, product_routes  # noqa: F401
