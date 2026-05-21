class User:
    def __init__(self, n, d):
        self.name = n
        self.date_creation = d

    @classmethod
    def create_user(cls, n, d):
        user = User(n, d)
        return user
