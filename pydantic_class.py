from pydantic import BaseModel


class User(BaseModel):
    name: str


# Validation + deserialization (deserializes to User)
user = User(name="Jeff")


# By default, validation is only at point of deserialization
user.name = ["no_error"]


# However, we can make validation occur whenever a setter is called
class CustUser(BaseModel, validate_assignment=True):
    name: str


user = CustUser(name="jeff")
user.name = ["error"]
