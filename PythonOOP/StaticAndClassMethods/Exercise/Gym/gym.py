class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self,trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription_searched = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        customer_searched = [customer for customer in self.customers if customer.id == subscription_searched.customer_id][0]
        trainer_searched = [trainer for trainer in self.trainers if trainer.id == subscription_searched.trainer_id][0]
        plan_searched = [plan for plan in self.plans if plan.id == trainer_searched.id][0]
        equipment_searched = [e for e in self.equipment if e.id == plan_searched.equipment_id][0]
        result = ''
        result = subscription_searched.__repr__() + '\n' + customer_searched.__repr__() + '\n'\
                 + trainer_searched.__repr__() + '\n' + equipment_searched.__repr__() + '\n' + plan_searched.__repr__()
        return result








