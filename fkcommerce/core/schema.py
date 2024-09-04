from . import marshmallow


class CategoryResponseSchema(marshmallow.Schema):
    id = marshmallow.Integer(dump_only=True)
    name = marshmallow.String(required=True)
    slug = marshmallow.String(required=True)


class CategoryInsertSchema(marshmallow.Schema):
    name = marshmallow.String(required=True)
    slug = marshmallow.String(required=True)
    is_active = marshmallow.Boolean(required=True)
    parent_id = marshmallow.Integer(allow_none=True)


class ProductInsertSchema(marshmallow.Schema):
    pid = marshmallow.Integer(dump_only=True)
    name = marshmallow.String(required=True)
    slug = marshmallow.String(required=True)
    description = marshmallow.String()
    is_digital = marshmallow.Boolean(required=True)
    is_active = marshmallow.Boolean(required=True)
    category_id = marshmallow.Integer()
    stock_status = marshmallow.String(dump_only=True)
    created_at = marshmallow.DateTime(dump_only=True)
    seasonal_event = marshmallow.Integer(allow_none=True)
    product_type_ids = marshmallow.List(marshmallow.Integer(), required=True)


class ProductLineInsertSchema(marshmallow.Schema):
    price = marshmallow.Decimal(places=2)
    sku = marshmallow.String(dump_only=True)
    stock_qty = marshmallow.Integer()
    is_active = marshmallow.Boolean(required=True)
    order = marshmallow.Integer()
    weight = marshmallow.Float()
    created_at = marshmallow.DateTime(dump_only=True)
    product_id = marshmallow.Integer()
    product_attribute_ids = marshmallow.List(marshmallow.Integer(), required=True)


class ProductImageInsertSchema(marshmallow.Schema):
    alternative_text = marshmallow.String(max_length=200)
    url = marshmallow.String()
    order = marshmallow.Integer()
    product_line_id = marshmallow.Integer()


class AttributeInsertSchema(marshmallow.Schema):
    name = marshmallow.String(max_length=200)
    description = marshmallow.String()


class SeasonalEventInsertSchema(marshmallow.Schema):
    start_date = marshmallow.DateTime(dump_only=True)
    end_date = marshmallow.DateTime(dump_only=True)
    name = marshmallow.String(max_length=100, required=True)


class ProductTypeInsertSchema(marshmallow.Schema):
    name = marshmallow.String(max_length=100)
    parent_id = marshmallow.Integer(allow_none=True)


class AttributeValueInsertSchema(marshmallow.Schema):
    attribute_value = marshmallow.String(max_length=100, required=True)
    attribute_id = marshmallow.Integer()


