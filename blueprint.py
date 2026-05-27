class Person:
    def __init__(self,name,age,city,country,amount=10):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        self.amout = amount

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print(f"Amount: {self.amout}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
country = input("Enter your country: ")
Amount = input("enter the amount")

person = Person(name, age, city, country)

person.show_info()

