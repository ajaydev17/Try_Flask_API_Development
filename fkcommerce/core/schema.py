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
