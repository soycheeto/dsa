grid = [
    [1, 2, 3, 2,3,1,3,2,1],
    [4,5,6,4,5,6,4,5,6],
    [7,8,9,7,8,9,8,9,7],
    [4,5,6,2,3,1,2,3,1],
    [1,2,3,5,4,6,4,5,6],
    [7,8,9,7,8,9,7,8,9],
    [8,7,9,1,3,2,3,1,2],
    [4,5,6,6,5,4,9,8,7],
    [2,3,1,7,9,8,4,6,5]
]


#Define a function that finds the sum across one row
def rowSum(grid):
    sum = 0
    for i in grid[0]:
        sum+=i
    print(sum)
rowSum(grid)

#Define a function that finds the sum across all rows
def rowSumAll(grid):
    sum=0
    for i in grid:
        for j in i:
            sum+=j
    print(sum)
rowSumAll(grid)

#Define a function that finds the sum across one column
def colSum(grid):
    sum=0
    for i in grid:
        sum+=i[0]
    print(sum)
colSum(grid)

#Define a function that finds the sum across all columns
def colSumAll(grid):
    sum=0
    for i in grid:
        for j in i:
            sum += j
    print(sum)
colSumAll(grid)

#Define a function that finds the sum across one sub-grid(given arguments will be starting row number and starting column number of the grid)
def sumSub(grid):
    sum=0
    for i in range(3):
        for j in range(3):
            sum+= grid[i][j]
    print(sum)
sumSub(grid)

#Define a function that finds the sum across all sub-grids
def sumSubAll(grid):
    sum=0
    for i in range(9):
        for j in range(3):
            for k in range(3):
                sum+=grid[j][k]
    print(sum)
sumSubAll(grid)

#Define a function that searches for an element across one grid
def gridSearch(grid):
    n = int(input("Enter a number from 1-9 to be searched:\n"))
    for i in range(9):
        for j in range(9):
            if grid[i][j]==n:
                return f"The first instance of {n} is at [{i}][{j}].\n"

print(gridSearch(grid))
