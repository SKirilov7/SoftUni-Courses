class Subscription:
    subs_id = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        Subscription.subs_id += 1
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.subs_id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @staticmethod
    def get_next_id():
        return Subscription.subs_id + 1





