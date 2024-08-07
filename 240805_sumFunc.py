def sumFunc(var1, var2):
    sum = var1+var2
    print(sum)

sumFunc(4,6)

list1 = [1,2,4,5,6]
sum=0

for i in list1:
    sum+=i
print(sum)

def sumList(list1):
    sum=0
    for i in list1:
        sum+=i
    print(sum)

sumList(list1)

def sumEven(list1):
    sum=0
    for i in list1:
        if i%2==0:
            sum+=i
    print(sum)

sumEven(list1)

def sumOdd(list1):
    sum=0
    for i in list1:
        if i%2!=0:
            sum+=i
    print(sum)

sumOdd(list1)

def prime(n):
    for i in range(2, n):
        if n%i==0:
            return f"{n} is composite.\n"

    return f"{n} is prime.\n"

prime(3301)

list1= [1,2,4,5,6]

def primeList(list1):
    for i in list1:
        print(prime(i))

primeList(list1)