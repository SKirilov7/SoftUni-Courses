class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        return "Not enough budget"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            searched_worker = [worker for worker in self.workers if worker_name == worker.name][0]
            self.workers.remove(searched_worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_amount = sum([worker.salary for worker in self.workers])
        if self.__budget >= salaries_amount:
            self.__budget -= salaries_amount
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_care_animals = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= money_for_care_animals:
            self.__budget -= money_for_care_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal.__repr__() for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal.__repr__() for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal.__repr__() for animal in self.animals if isinstance(animal, Cheetah)]

        result = f'You have {len(self.animals)} animals\n'
        result += f'----- {len(lions)} Lions:\n'
        result += '\n'.join(lions) + '\n'
        result += f'----- {len(tigers)} Tigers:\n'
        result += '\n'.join(tigers) + '\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += '\n'.join(cheetahs)
        return result

    def workers_status(self):
        keepers = [worker.__repr__() for worker in self.workers if isinstance(worker, Keeper)]
        caretakers = [worker.__repr__() for worker in self.workers if isinstance(worker, Caretaker)]
        vets = [worker.__repr__() for worker in self.workers if isinstance(worker, Vet)]
        result = f'You have {len(self.workers)} workers\n'
        result += f'----- {len(keepers)} Keepers:\n'
        result += '\n'.join(keepers) + '\n'
        result += f'----- {len(caretakers)} Caretakers:\n'
        result += '\n'.join(caretakers) + '\n'
        result += f'----- {len(vets)} Vets:\n'
        result += '\n'.join(vets)
        return result
