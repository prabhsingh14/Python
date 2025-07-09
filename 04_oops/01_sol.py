class Car:
    #constructor
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def hello(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    #static method
    @staticmethod
    def description():
        return "This is a car class"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def fuel_type(self):
        return "Electricity"

tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.battery)
print(tesla.hello())
print(tesla.model)
print(tesla.get_brand())
print(tesla.fuel_type())

my_car = Car("Toyota", "Camry")
print(my_car.get_brand())
print(my_car.hello())
print(my_car.fuel_type())
print(my_car.model)

print(Car.description())
print(ElectricCar.description()) 