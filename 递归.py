def greet(name):
    print ("hello")
    greet2(name)
    print ("getting ready to say goodbye")
    bye()
def greet2(name):
    print ("How are you?")
def bye():
    print ("OK,Bye!")
def greet(name):
    print ("hello")
def greet2(name):
    print("How are you?")
def f(x):
    if x == 1:
        return 1
    else:
        return x * f(x-1)
