username = "atiqurrahman"

def func():
    # username = "anis"
    print(username)

print(username)
func()


x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 12
    
# func3()
# print(x)


# closure example # A closure is a function that remembers the environment in which it was created, even after that environment has finished executing.
# A closure allows the inner function to access variables from the outer function's scope even after the outer function has finished executing.
def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()

# closure example with parameters
def closure_func(num):
    def actual(x):
        return x ** num
    return actual



f = closure_func(2) # this will take memory references of the actual function and its variables references
g = closure_func(3)

print(f(3))
print(g(3))