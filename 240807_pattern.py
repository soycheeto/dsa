import math

def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("1 ", end="")
        print()

pattern(5)

"""Print the following pattern
1
1 1
1 1 1
1 1 1 1"""

def patternYi():
    for i in range(5):
        for j in range(i):
            print("1 ", end="")
        print()
    
patternYi()

"""Print the following pattern
2
2 2
2 2 2
2 2 2 2
2 2 2 2 2"""

def patternEr():
    for i in range(6):
        for j in range(i):
            print("2 ", end="")
        print()
patternEr()

"""Print the following pattern
1
2 2
3 3 3
4 4 4 4"""

def patternGe():
    for i in range(1,5):
        for j in range(i):
            print(f"{i} ", end="")
        print()

patternGe()

"""Print the following pattern
111111111
222222222
333333333
444444444
555555555"""

def patternFin():
    for i in range(1,6):
        for j in range(10):
            print(i, end="")
        print()
patternFin()