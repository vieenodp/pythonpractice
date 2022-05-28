def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper


def f():
    print("Hello")

x = f1(f)  # This line can be replaced with @f1 which is called decorator, check dec-ex5 for it.
x()
