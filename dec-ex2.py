def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper


def f():
    print("Hello")

f1(f)()