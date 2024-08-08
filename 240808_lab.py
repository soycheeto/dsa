"""Write a program to find the largest and smallest element in the given array [1,2,3,5,6,7]( Provide two different functions for find the largest  element and the smallest element in an array respectively)"""

def largest(unArray):
    largest = unArray[0]
    for i in unArray:
        if i>largest:
            largest=i
    print(largest)

def least(unArray):
    least = unArray[0]
    for i in unArray:
        if i<least:
            least=i
    print(least)

largest([1,2,3,5,6,7])
least([1,2,3,5,6,7])


"""[1,2,3,5,6,7]- Sort the array in the ascending order and then in the descending order"""

def arrSort(arr):
    sortAsc = []
    while arr:
        least = arr[0]
        for i in arr:
            if i<least:
                least = i
        sortAsc.append(least)
        arr.remove(least)
    print(sortAsc)
    print(sortAsc[::-1])

arrSort([1,2,3,5,6,7])



"""Write a program to find the second  largest and second smallest element in the given list [1,3,2,5,6,7]( Provide two different functions for find the  second largest  element and the  second smallest element in an array respectively)"""

def secLargest(arr):
    setArr = set(arr)
    arr = list(setArr)
    largest = arr[0]
    for i in arr:
        if i>largest:
            largest = i
    arr.remove(largest)
    secLargest = arr[0]
    for i in arr:
        if i>secLargest:
            secLargest=i
    print(secLargest)

secLargest([1,2,3,5,6,7,7])

def secLeast(arr):
    setArr = set(arr)
    arr = list(setArr)
    least = arr[0]
    for i in arr:
        if i<least:
            least = i
    arr.remove(least)
    secLeast =arr[0]
    for i in arr:
        if i<secLeast:
            secLeast = i
    print(secLeast)
secLeast([1,1,2,3,5,6,7])
