import math
def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n==1:
            break
        if n%i==0:
            return f"{n} is composite.\n"

    return f"{n} is prime.\n"

prime(3301)

list1= [1,2,4,5,6]

def primeList(list1):
    for i in list1:
        print(prime(i))

primeList(list1)

#Write a program that takes a positive integer N and prints the sum of the first N natural numbers.

def sumN():
    n = int(input("Enter a positive integer: \n"))
    sum=0
    for i in range(n+1):
        sum+=i
    return f"The sum of the first {n} numbers is {sum}"

print(sumN())

#Write a program that takes a positive integer N and prints the factorial of N

def nFactorial():
    n = int(input("Enter a positive integer: \n"))
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    return factorial

print(nFactorial())
#Write a program that prints all prime numbers between 1 and 100

def limitPrime():
    for num in range(2, 101):
        for i in range(2, int(math.sqrt(num))+1):
            if num%i==0:
                break
        else:
            print(num)
limitPrime()    
#Write a program that takes a number as input and prints its multiplication table of a particular number

def nMultiples():
    n = int(input("Enter a positive integer: \n"))
    for i in range(1,12):
        print(i, "x", n, "=", i*n)
    
nMultiples()
#Write a program that takes a number and prints the fibonacci number of that particular number
def fibonacci():
    a,b= 1,1
    t,n = 0,0
    iter = int(input("Enter the no. of iterations:\n"))
    while(n<iter):
        t=a
        a+=b
        b=t
        n+=1
    return f"The fibonacci number after {iter} iterations is {a}\n"

print(fibonacci())