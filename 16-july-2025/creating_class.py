"""The following code consists of a simple class with simple implementation"""

class Car:
    # self keywords refers to => jis ne bhi call kiya
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def print_deets(self):
        print(f'Brand: {self.brand}\n'
              f'Model: {self.model}')

# car1 = Car("Toyota", "Corolla")
# car1.print_deets()

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def print_deets(self):
        print(f'Brand: {self.brand}\n'
              f'Model: {self.model}\n'
              f'Battery Size: {self.battery_size}')


car = ElectricCar("Tesla", "Model S", "85kwh")
print(car.print_deets())
