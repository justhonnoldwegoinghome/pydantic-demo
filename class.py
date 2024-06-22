class User:
    name: str

    def __init__(self, name: str):
        self.name = name


# No validation
user = User(["Jeff"])
