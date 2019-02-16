"""
name: Fiona Cremins
student number: 118301286
desc: Classes and Objects

"""

class Car:
    """
    car has 4 instance variables and 3 attributes
    __year - int - this represents the year of te car
    __make - string - this represents the make of the car
    __model - string - this represents the model of the car
    __speed - int - current speed of the car
    """
    def __init__(self, year, make, model):
        # Constructor
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0

    # this accelerates the car by adding 5 to the speed
    def accelerate(self):
        self.__speed += 5
        return self.__speed

    # this decelerates the car by taking 5 from the speed
    def brake(self):
        self.__speed -= 5

    # this gets the current speed
    def get_speed(self):
        return self.__speed

    # this outputs a string of the current instance
    def __str__(self):
        return str(self.__year) + ' ' + self.__make + ' ' + self.__model + ' ' + str(self.__speed)
