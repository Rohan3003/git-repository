# Given a positive number N, you need to find factorial of this number
# Factorial - product of number in the range 1 to N

# 1! - 1
# 2! - 1*2
# 3! - 1*2*3
# 4! - 1*2*3*4 = 4 * factorial(3)

N = int(input())

def factorial(N : int):
    if N < 1:
        return "Invalid Input"
    elif(N == 1):
        return N
    else:
        return N * factorial(N-1)
        

fact_N = factorial(N)
print(fact_N)