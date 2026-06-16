# username = "nileshnarwade"

# def name():
#     # username = "chai"
#     print(username)

# print(username)
# name()


x = 99
#  def func(y):
#      z = x+y
#      return z

#  print(func(1))


# def fucn3():
#     global x
#     x = 88

# fucn3()
# print(x)


def f1():
    x= 88
    def f2():
        print(x)
    return f2

result = f1()
result()

# closures example
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(2))
print(g(3))


