# Sum of Natural Numbers using Recursion

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

n = int(input("Enter a number: "))
print("Sum of natural numbers =", sum_n(n))
