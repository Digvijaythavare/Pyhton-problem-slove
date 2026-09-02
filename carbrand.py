class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting.")

brand = input("Enter the car brand: ")
model = input("Enter the car model: ")
year = input("Enter the car year: ")                                                                                                                        
prics = int(input("Enter the car price: "))

car1 = car(brand, model, year)
car1.display_info()
car1.start_engine()