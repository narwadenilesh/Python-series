# def decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper


# @decorator
# def greet():
#     print("Hello!")

# greet()


def decorator(func):
    def wrapper(a, b):
        print("Adding numbers...")
        result = func(a, b)
        print("Addition completed.")
        return result
    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(10, 20))

