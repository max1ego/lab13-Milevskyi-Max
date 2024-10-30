class COMP:
    def __init__(self, model, inventory_number, price):
        self.model = model
        self.inventory_number = inventory_number
        self.price = price
        print(f"Комп'ютер {self.model} створено з інвентарним номером {self.inventory_number} та ціною {self.price}.")

    def __del__(self):
        print(f"Комп'ютер {self.model} з інвентарним номером {self.inventory_number} видалено.")

    def change_inventory_number(self, new_inventory_number):
        self.inventory_number = new_inventory_number
        print(f"Інвентарний номер змінено на {self.inventory_number}.")

    def change_price(self, new_price):
        self.price = new_price
        print(f"Ціна змінена на {self.price}.")

    def __str__(self):
        return f"Модель: {self.model}, Інвентарний номер: {self.inventory_number}, Ціна: {self.price}"

computers = [
    COMP("ModelA", 1001, 1500),
    COMP("ModelB", 1002, 1600),
    COMP("ModelC", 1003, 1400),
    COMP("ModelD", 1004, 1550),
    COMP("ModelE", 1005, 1650),
    COMP("ModelF", 1006, 1300),
    COMP("ModelG", 1007, 1700)
]

for comp in computers:
    print(comp)

computers[0].change_inventory_number(2001)
computers[0].change_price(1550)
print(computers[0])

print("\n--- Видалення всіх об'єктів ---")
del computers
