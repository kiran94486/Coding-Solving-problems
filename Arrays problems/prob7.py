#BUBBLE SORT IN PYTHON
#example 1
# def bubblesort(arr,n):
#     for i in range(n-1):
        
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

#     return arr

# arr=[64, 34, 25, 12, 22, 11, 90]

# n=len(arr)
# sort=bubblesort(arr,n)
# print("sorted array :"+str(sort))

#example 2
def bubble(array,n_size):
    for i in range(n_size):

        for j in range(0,n_size-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array



array=[87,45,65,32,98,42,55,21,11]
n_size=len(array)
bub=bubble(array,n_size)
print("sorted array :"+str(bub))

#Example x

def bubblbl(arry,ns):
    for i in range(ns):
        for j in range(0,ns-i-1):
            if arry[j] > arry[j+1]:
                arry[j],arry[j+1]=arry[j+1],arry[j]
    return arry


arry=[78,54,66,33,22,66,0]
ns=len(arry)
bb=bubblbl(arry,ns)
print("sorted array = "+str(bb))