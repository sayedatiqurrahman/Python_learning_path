#n = int(input("Enter a positive integer: "))
n= 30

sum_of_positive_numbers = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        # print(f"{i} is even")
        sum_of_positive_numbers += i


print(f"Sum of positive even numbers from 1 to {n}: {sum_of_positive_numbers}")
