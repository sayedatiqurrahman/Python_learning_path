class Car:
    total_cars = 0  # Class variable to keep track of total cars created
    # This class represents a car with brand and model attributes.
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1  # Increment the total cars count when a new car is created
   
    # method to return the full name of the car
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Gasoline , Diesel or Petrol"

    # 07. static method to return a general description of a car
    @staticmethod
    def general_description():
        return "This is a car."
    
    #  08. property decorator example ______________
    @property
    def model(self):
        return self.__model
    
# this code allow you to set value to model attribute
    # @model.setter
    # def model(self, value):
    #     self.__model = value
    


#  instance of the Car class
my_car = Car("Toyota", "Corolla")
# print(f"My car is a {my_car.brand} {my_car.model}.")
# # This code defines a simple class `Car` with an initializer that sets the brand and model of the car.

new_car = Car("Honda", "Civic")
# print(new_car.full_name())

#  03. inheritance example ______________
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size=75):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge or Battery"




tesla = ElectricCar("Tesla", "Model S", 100)
# 02. class Method example ______________ 
# print(f"My electric car is a {tesla.full_name()} with a {tesla.battery_size}-kWh battery.")

# 04. Encapsulation Private attribute example ______________
# print(tesla.__brand)  # This will raise an AttributeError because __brand is private
# print(tesla.get_brand())  # this is the only way to access the private attribute __brand

# 05. Polymorphism example _______________
# print(tesla.fuel_type())  # This will print "Electric Charge or Battery"
# print(my_car.fuel_type())  # This will print "Gasoline , Diesel or Petrol"


# 06. class variable ____________________
# print(f"Total cars created: {Car.total_cars}")  # This will print the total number of car instances created

# print(Car.general_description())


# property decorator example
# tesla.model = "Model X"  # This will raise an AttributeError because model is not a property
# print(tesla.model)



# 09. inheritance and isinstance example ______________
# print(isinstance(tesla, ElectricCar))  # This will print True
# print(isinstance(tesla, Car))  # This will also print True, since ElectricCar is a subclass of Car
# print(isinstance(my_car, ElectricCar))  # This will print False.




# 10. Multiple Inheritance example ______________
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    def battery_info(self):
        return f"Battery size: {self.battery_size} kWh"


class Engine:
    def engine_info(self):
        return "Engine type: Electric"


class NewElectricCar(Battery, Engine, Car):
    def __init__(self, brand, model, battery_size=75):
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery_size)
        Engine.__init__(self)


    def fuel_type(self):
        return "Hybrid: Electric Charge and Gasoline"
    
    def full_name(self):
        return f"{self.get_brand()} {self.model} Hybrid"
    


my_new_electric_car = NewElectricCar("Toyota", "Prius", 50)

print(my_new_electric_car.battery_info())
print(my_new_electric_car.engine_info())