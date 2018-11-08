x = 50

def func():
    # global x
    x = 1000
    return x

print("before function call, x is: ",x)
x = func()
print("after function call, x is: ",x)
