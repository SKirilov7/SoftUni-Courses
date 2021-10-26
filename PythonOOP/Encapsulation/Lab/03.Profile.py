class Profile:
    MINIMAL_PASSWORD_LENGTH = 8

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not Profile.is_length_enough(value) or not Profile.is_there_a_number(value) \
                or not Profile.is_there_a_uppercase_letter(value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    @staticmethod
    def is_length_enough(value):
        return len(value) >= Profile.MINIMAL_PASSWORD_LENGTH

    @staticmethod
    def is_there_a_number(value):
        numbers = [char for char in value if char.isdigit()]
        return True if numbers else False

    @staticmethod
    def is_there_a_uppercase_letter(value):
        uppercase_letters = [char for char in value if char.isupper()]
        return True if uppercase_letters else False

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
