#  Fibonacci series is a pattern of number where each number is sum of preceding two number and it starts with 0 and 1
# N = 5 -> 0 1 1 2 3 5 8

N = int(input())
fib_list = []
def Fibonacci(N):
    if N == 1:
        fib_list.append(N)
    elif N == 2:
        fib_list.append(N)
        fib_list.append(N-1)
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

fib_N = Fibonacci(5)
print(fib_N)


