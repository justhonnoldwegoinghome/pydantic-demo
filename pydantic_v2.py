"""
Basic guide on how to use Pydantic V2.
"""

from pydantic import BaseModel, Field, field_validator, EmailStr, ValidationError


class User(BaseModel):
    # [Concept: Default values]
    ## If a field has a default value, it becomes optional when creating a model instance.
    name: str = "jeff"

    # [Concept: Custom validation]
    ## `mode` determines whether custom validator is ran before or after pydantic default validator.
    age: int = Field(ge=3)

    @field_validator("age", mode="before")
    @staticmethod
    def validate_age(val):
        # (*) validators should either return the parsed value or raise a ValueError or AssertionError (assert statements may be used).
        if val < 5:
            raise ValueError("Must be at least 5 years old.")

    # [Concept: using Pydantic's types]
    email: EmailStr


try:
    user = User(age=1, email="ok@gmailcom")
except ValidationError as e:

    from pprint import pprint

    pprint(e.errors())
