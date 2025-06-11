def factorial(n):
    if n == 0:
        print(f" inner side of if Calculating factorial of {n}")
        return 1
    else:
        print(f" inner side of else Calculating factorial of {n}")
        return n * factorial(n - 1)
    


print('final output:  ',factorial(5))  # Output: 120