def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper


def f():
    print("Hello")

f = f1(f)
f()
