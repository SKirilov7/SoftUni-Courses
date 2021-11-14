class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = []

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for current_list in args:
            for element in current_list:
                result += element.get_monthly_expense()
        self.expenses = result

    def calculate_appliances_expenses(self):
        result = 0
        for appliance in self.appliances:
            result += appliance.get_monthly_expense()
        return result

    def __repr__(self):
        result = ''
        result += f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$," \
                  f" Expenses: {self.expenses:.2f}$\n"
        if self.children:
            n = 1
            for children in self.children:
                result += f"--- Child {n} monthly cost: {(children.get_monthly_expense()):.2f}$\n"
                n += 1
        result += f'--- Appliances monthly cost: {sum(appliance.get_monthly_expense() for appliance in self.appliances):.2f}$\n'
        return result
