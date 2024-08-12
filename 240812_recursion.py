#Write a python program to find the sum of n natural numbers using recursion
def sumFunc(n):
    if n >= 1:    
        return n + sumFunc(n-1)
    else:
        return 0
    
print(sumFunc(5))

#Write a python program to find the factorial of a number using recursion

def factorial(n):
    if n>=1:
        return n * factorial(n-1)
    else:
        return 1
print(factorial(5))

#Write a python program to find the fibonacci number of a given term using recursion

def fibonacci(iter, a=1, b=1, n=1):
    if n < iter:
        return fibonacci(iter, b, a + b, n + 1)
    else:
        return f"The Fibonacci number after {iter} iterations is {a}\n"

print(fibonacci(10))
