class Child:
    DAYS_IN_MONTH = 30

    def __init__(self, food_cost, *toys_cost):
        self.cost = food_cost + sum([toy for toy in toys_cost])

    def get_monthly_expense(self):
        return self.cost * Child.DAYS_IN_MONTH
