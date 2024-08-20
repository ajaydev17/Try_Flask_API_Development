from . import marshmallow


class CategorySchema(marshmallow.Schema):
    id = marshmallow.Integer(dump_only=True)
    name = marshmallow.String(required=True)
    slug = marshmallow.String(required=True)
