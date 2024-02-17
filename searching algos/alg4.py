# Ternary search


def ternary_search(array,l,r,key):
    while l<=r:
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3

        if array[mid1]==key:
            return mid1
        if array[mid2]==key:
            return mid2
        if array[mid1]<key:
            l=mid1+1
        elif array[mid2]>key:
            r=mid2-1
        else:
            l=mid1+1
            r=mid2-1
    return -1


array=[10,20,30,40,50,60,70,80]
n=len(array)
key=50
result = ternary_search(array,0,n-1,key)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Target is not present in this array")