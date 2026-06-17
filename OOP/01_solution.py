class Car:
    # static varibale shares the same value across all instances
    total_cars = 0;
    # constructor
    def __init__(self, brand,  model):
        # __ means make a variable private / encapsulation
        self.__brand = brand
        self.__model = model
        Car.total_cars+= 1;

    def get_brand(self):
        return self.__brand + "!"


    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "petrol or diesel"

    # decorators in python
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model



# inheritance
class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
            return "Electric charge"


my_tesla = Electric_car("Tesla", "Model S", "85KWH")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, Electric_car))
# print(my_tesla.fuel_type())

# print(my_tesla.brand)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())


my_car = Car("Toyota", "Corolla")
# print(my_car.full_name())

# i want to prevent this modification so make the model read only attribute
# my_car.model = "City" 
# print(my_car.model())

# print(Car.general_description())
# print(my_car.general_description())


# my_new_car = Car("Tata", "Safari")
# print(my_new_car.fuel_type())

# print(Car.total_cars)
# test_car = Car("Tst", "tst")
# print(my_new_car.total_cars)
# print(test_car.total_cars)

# multiple inheritance
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class Electric_car2(Battery, Engine, Car):
    pass


my_new_tesla = Electric_car2("Tesla", "Model S")

print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())