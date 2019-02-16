"""
name: Fiona Cremins
desc: Classes and Objects
"""

import car

car = car.Car(2005, "Audi", "A4")

print("car accelerates")


car.accelerate()
print(car.get_speed())
car.accelerate()
print(car.get_speed())
car.accelerate()
print(car.get_speed())
car.accelerate()
print(car.get_speed())
car.accelerate()
print(car.get_speed())

print("car decelerates")

car.brake()
print(car.get_speed())
car.brake()
print(car.get_speed())
car.brake()
print(car.get_speed())
car.brake()
print(car.get_speed())
car.brake()
print(car.get_speed())
