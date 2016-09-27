
def adder(number_one, number_two, message="No message passed", happy=True):
    print (message)
    print (happy)
    return number_one + number_two

print (adder(9, 4, message="Do math son!", happy=False))

print (adder("Joel", " likes programming"))


def add(*args):
    return sum(args)

print (add(1, 2, 4, 44, 88))

print (adder(*[9, 4]))

print (add(*range(100)))


def beginners_luck(name, account_number, *args, **kwargs):
    print (name, "Name")
    print (account_number, "Account Number")
    print (args)
    print (kwargs)
    return 1

print (beginners_luck("Sam", 2916325, [1, 2, 4], birthday="March 21"))
