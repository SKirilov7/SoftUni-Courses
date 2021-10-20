class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += customer.__repr__() + '\n'
        for dvd in self.dvds:
            result += dvd.__repr__() + '\n'
        return result

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        searched_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        customer = [cust for cust in self.customers if cust.id == customer_id][0]
        if searched_dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {searched_dvd.name}"
        if searched_dvd.is_rented:
            return f"DVD is already rented"
        if searched_dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {searched_dvd.age_restriction} to rent this movie"
        searched_dvd.is_rented = True
        customer.rented_dvds.append(searched_dvd)
        return f"{customer.name} has successfully rented {searched_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        searched_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        customer = [cust for cust in self.customers if cust.id == customer_id][0]
        if searched_dvd in customer.rented_dvds:
            customer.rented_dvds.remove(searched_dvd)
            searched_dvd.is_rented = False
            return f"{customer.name} has successfully returned {searched_dvd.name}"
        return f"{customer.name} does not have that DVD"







