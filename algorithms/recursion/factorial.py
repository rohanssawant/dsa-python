def iterative_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# print(iterative_factorial(0))
# #1
# print(iterative_factorial(5))
# #120
# print(iterative_factorial(50))


def recursive_factorial(n):
    # base case
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)


print(recursive_factorial(0))
#1
print(recursive_factorial(5))
#120
print(recursive_factorial(50))
#30414093201713378043612608166064768844377641568960512000000000000