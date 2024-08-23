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
