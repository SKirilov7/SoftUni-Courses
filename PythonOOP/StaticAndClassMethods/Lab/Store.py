class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


    @staticmethod
    def can_add_item(dict_of_items,capacity):
        count = sum([count for item, count in dict_of_items.items()])
        return count < capacity

    @staticmethod
    def can_remove_items(dict_items, item, amount_to_remove):
        return item in dict_items and dict_items[item] >= amount_to_remove


    @classmethod
    def from_size (cls, name:str, type:str, size:int):
        return cls(name, type, size // 2)

    def add_item(self, item_name:str):
        count = sum([count for item,count in self.items.items()])
        if not self.can_add_item(self.items, self.capacity):
            return "Not enough capacity in the store"

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name:str, amount:int):
        if not self.can_remove_items(self.items,item_name,amount):
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            self.items.pop(item_name)

        return f"{amount} {item_name} removed from the store"




first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))







