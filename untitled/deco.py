def greetmain(a,b):
    def greet():
        print(a,b)
    return greet
x=greetmain(10,20)
x()