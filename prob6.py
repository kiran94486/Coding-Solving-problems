 #selection sort in python

def selection_sort(A,n):

    for i in range(n):
        min_indx=i
        for j in range(i+1,n):
            if A[min_indx]>A[j]:
                min_indx = j
        
        # Swapping
        A[i],A[min_indx]=A[min_indx],A[i]


    return A

A=[64, 25, 12, 22, 11]
n=len(A)

sort_array=selection_sort(A,n)
print("sORTED ARRAY:")
print(sort_array)

# Complexity Analysis of Selection Sort
# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:

# One loop to select an element of Array one by one = O(N)
# Another loop to compare that element with every other Array element = O(N)
# Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)
# Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. The selection sort never makes more than O(N) swaps and can be useful when memory writing is costly. 

# Advantages of Selection Sort Algorithm
# Simple and easy to understand.
# Works well with small datasets.
# Disadvantages of the Selection Sort Algorithm
# Selection sort has a time complexity of O(n^2) in the worst and average case.
# Does not work well on large datasets.
# Does not preserve the relative order of items with equal keys which means it is not stable.



#Example2

def sel_sort1(arr,lens):
    for i in range(lens):
        minin_index=i
        for j in range(i+1,lens):
            if arr[minin_index]>arr[j]:
                minin_index=j

        arr[i],arr[minin_index]=arr[minin_index],arr[i]

    return arr


arr=[5,8,2,4,9,4,1]
lens=len(arr)
selectionsort=sel_sort1(arr,lens)
print("Sorted array:"+ str(selectionsort))




#example 3

def sel(array,n_size):
    for i in range(n_size):
        minimum=i
        for j in range(i+1,n_size):
            if array[minimum]>array[j]:
                minimum=j
        #swapping
        array[i],array[minimum]=array[minimum],array[i]

    return array

array=[7,4,9,2,6,4,1]
n_size=len(array)
seelle=sel(array,n_size)
print("Sorted array :"+str(seelle))


#example 4
def sls(arry,ns):
    for i in range(ns):
        mmmid=i
        for j in range(i+1,ns):
            if arry[mmmid]>arry[j]:
                mmmid=j
        arry[i],arry[mmmid]=arry[mmmid],arry[i]
        
    return arry



arry=[56,32,87,44,21,11]
ns=len(arry)
outpt=sls(arry,ns)
print(outpt)




