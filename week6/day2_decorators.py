
def func_caller(func):
    print ("hello")
    return func


@func_caller
def remote_control():
    print ("I love lamp")
    return 0

print (remote_control())

# func_caller(remote_control)
