import sys

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def dynamic_fibonacci(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        result = dynamic_fibonacci(n - 1, memo) + dynamic_fibonacci(n - 2, memo)
        memo[n] = result

        return result

if __name__ == '__main__':
    sys.setrecursionlimit(2700)
    n = int(input('Numero fibonacci:   '))
    # result = fibonacci(n)
    result = dynamic_fibonacci(n)
    print(result)