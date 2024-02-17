# Linear search

def linear_search(array,n,key):
    for i in range(0,n-1):
        if array[i]==key:
            return i
    





array=[10, 50, 30, 70, 80, 20, 90, 40]
n=len(array)
key=70

ls=linear_search(array,n,key)
print(str(key)+"is found in index"+str(ls))