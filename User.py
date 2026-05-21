class User:
    def __init__(self, n, d):
        self.name = n
        self.date_creation = d

    @classmethod
    def create_user(cls, n, d):
        user = User(n, d)
        return user
    
    def view_profile(self):
        print(f"===Your Account Info=== \nName: {self.name} \nAccount created on: {self.date_creation}")

