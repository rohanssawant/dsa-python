def recur_fib(n):
    if n == 1:                                  # Base case 1
        return 1
    if n == 0:                                  # Base case 1
        return 0
    return recur_fib(n-1) + recur_fib(n-2)      # Recur case where soln = sum of previous two numbers
