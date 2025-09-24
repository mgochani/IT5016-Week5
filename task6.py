def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(123, is_even(123))
print(20, is_even(20))

def find_max(a, b):
    if (a > b):
        return a
    return b

print(find_max(find_max(120, 6), 20))


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    ans = 1
    for i in range(1, n + 1):
        ans *= i

    return ans

factorial(4)