# def my_decorator(func):
#     def wrapper():
#         print('Before calling the function')
#         func()
#         print('After calling the function')
#     return wrapper


# @my_decorator
# def say_hello():
#     print("Rakesh")

# say_hello()










# def mydecorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

def mydecorator(func):
    def wrapper(name):
        print("Before function call")
        func(name)
        print("After function call")
    return wrapper



@mydecorator
def say_hello(name):
    print(f"name is : {name}")


say_hello("Rakesh")
