print ("Sam" + " programs")


class SuperNumber:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return SuperNumber(str(self.value) + str(other.value))
             # ^^ creating instance of class inside of class

    def __str__(self):
        return "Debug: Value is " + str(self.value)


s_number_1 = SuperNumber(1)
s_number_2 = SuperNumber("Sam")

print (s_number_1)

x = s_number_1 + s_number_2 + s_number_2

print (x)
