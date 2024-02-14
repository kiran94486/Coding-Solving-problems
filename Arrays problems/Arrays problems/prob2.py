 # Program to find the minimum (or maximum) element of an array
def get_min(arr,n):

    min_temp = arr[0]
    for i in range(1,n):
        if arr[i] <= min_temp:
            min_temp=arr[i]
    print(min_temp)

def get_max(arr,n):
    max_temp=arr[0]

    for i in range(1,n):
        max_temp=arr[i]
    print(max_temp)

arr=[1,7,3,42,5,13]
n=len(arr)
get_min(arr,n)
get_max(arr,n)