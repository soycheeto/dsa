grid = [[1,2,3,4],[5,6,7,8,],[9,10,11,12],[13,14,15,16]]

#Find the sum of all elements across one row

def rowSum(grid):
    sum = 0
    for i in grid[0]:
        sum+=i
    print(sum)
rowSum(grid)

#Find the sum of all elements across all rows

def rowSumAll(grid):
    sum=0
    for i in grid:
        for j in i:
            sum+=j
    print(sum)
rowSumAll(grid)

#Find the sum of all elements across one coloumn

def colSum(grid):
    sum=0
    for i in grid:
        sum+=i[0]
    print(sum)
colSum(grid)

#Find the sum of all elements across all coloumns

def colSumAll(grid):
    sum=0
    for i in grid:
        for j in i:
            sum += j
    print(sum)
colSumAll(grid)

#Find the sum of all diagonal elements

def sum_diagonals(grid):
    d1 = 0
    d2 = 0

    for i in range(4):
        d1 += grid[i][i]
        d2 += grid[i][4 - 1 - i]
    
    return f"main diagonal sum is {d1} and secondary diagonal sum is {d2}"

print(sum_diagonals(grid))