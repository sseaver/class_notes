
class Person:

    def __init__(self, name):
        self.name = name

class Bike:

    def __init__(self, speeds, owner):
        self.speed = speeds
        self.owner = owner
        self.color = "grey"
        self._layers = 1


    def set_color(self, color):
        self._layers += 1
        self.color = color

    def get_layers(self):
        return self._layers

Sam = Person("Sam")
joel = Person("Joel")
bike = Bike(18, joel)
sams_bike = Bike(24, Sam)

print ("Owners=======")
print (bike.owner.name)
print (sams_bike.owner.name)

print (bike)
print ("color before we change it")
print (bike.color)
print (bike.get_layers)

print ("color after we change it")
bike.set_color("purple")
print (bike.color)
print (bike.get_layers)

print ("color of sams bike")
bike.set_color("orange")
print (sams_bike.color)
