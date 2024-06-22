from marshmallow import Schema
from marshmallow import fields


# This is a UserSchema, not a User class
class UserSchema(Schema):
    name = fields.Str(required=True)


# Validation + deserialization (but deserializes only to a dictionary)
user = UserSchema().load({"name": "Jeff"})


# Validation is only at point of deserialization
user["name"] = ["no_error"]
print(user)
