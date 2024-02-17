# Binary search

def binary_search(array,l,r,key):

    while l<=r:
        mid=l+(r-l)//2

        if array[mid]==key:
            return mid
        elif array[mid]<key:
            l=mid + 1
        else:
            r=mid - 1
    return -1
        


array=[2, 3, 4, 10, 40]
key=40
n=len(array)
bs=binary_search(array,0,n-1,key)
if bs != -1:
    print("Element is present at index", bs)
else:
    print("Element is not present in array")