# Sentinel - linear search


def sentimental_ls(array,n,key):
    last = array[n-1]

    array[n-1]=key

    i=0

    while array[i]!=key:
        i=i+1

    array[n-1]=last

    if ((i < n - 1) or (array[i] == key)):
        print(key,"is present at index",i)
    else:
        print("Element not found")
    



array=[10, 20, 180, 30, 60, 50, 110, 100, 70]
n=len(array)
key=60
sentimental_ls(array,n,key)