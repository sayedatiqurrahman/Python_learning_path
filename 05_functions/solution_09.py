# 👉  jump to: >>> 🔄 YIELD GUIDE markdown preview mode (scroll down) <<<




# usually , we are thinking using this way...

def even_num (x):
    list_of_even = []

    for i in range(1, x + 1):
        if i % 2 == 0:
            list_of_even.append(i)

    return list_of_even


# print(even_num(10))  # Output: [2, 4, 6, 8, 10]




# <=================================================================================================>


# we need to send a single value at a time, so we can use a generator function
# using a generator function to yield even numbers up to a given number

def even_num_generator(i):
    for i in range(2, i + 1, 2):
            yield i


print(even_num_generator(10))  # Output: <generator object even_num_generator at 0x...>

# to get the values from the generator, we can use a for loop or convert it to a list
print(list(even_num_generator(10)))  # Output: [2, 4, 6, 8, 10]


# or we can use a for loop to iterate through the generator
for num in even_num_generator(10):
    print(num)  # Output: 2, 4, 6, 8, 10 (each on a new line)


# or we can use the next() function to get the next value from the generator
gen = even_num_generator(10)
print(next(gen))  # Output: 2
print(next(gen))  # Output: 4
# and so on...

