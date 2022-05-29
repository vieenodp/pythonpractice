
def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    return wrapper

@f1
def f(a, b=9):
    print(a,b)

f("Hi!")





