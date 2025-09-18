class Car:
    def __init__(self, brand, model, year):
        self.brand = brand,
        self.model = model,
        self.year = year
    

    def display_info(self):
        print(f"This is a {self.year} {self.brand} {self.model}")

    

car1 = Car ("Infiniti", "G35",2010)
car2 = Car ("Toyota", "Seinna", 2024)

car1.display_info()
car2.display_info()

    

    