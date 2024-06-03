#  Fibonacci series is a pattern of number where each number is sum of preceding two number and it starts with 0 and 1
# N = 7 -> 0 1 1 2 3 5 8   -> sum = 20

# to get the next fibonacci number 
N = int(input())
def Fibonacci(N):
    if N == 1:
        return 0
    elif N == 2:
        return 1
    elif N == 3:
        return 2
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

fib_N = Fibonacci(N)
print(fib_N)