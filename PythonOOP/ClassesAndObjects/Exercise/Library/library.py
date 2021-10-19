class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        try:
            user_with_name_to_change = [u for u in self.user_records if u.user_id == user_id][0]
            old_name = user_with_name_to_change.username
            if not old_name == new_username:
                user_with_name_to_change.username = new_username
                if old_name in self.rented_books:
                    self.rented_books[user_with_name_to_change] = self.rented_books[old_name]
                    del self.rented_books[old_name]
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            return f"Please check again the provided username - it should be different than the username used so far!"
        except IndexError:
            return f"There is no user with id = {user_id}!"




