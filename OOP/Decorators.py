def mydecorator(function):
    
    def wrapper():
        print("Before wrapper")
        function()
        print("After wrapper")
    return wrapper

@mydecorator    
def hello_world():
    print("Hello World !")
    
mydecorator = mydecorator(hello_world)()

hello_world()
