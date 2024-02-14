# Array Reverse in Python

#here i took 2 variables start and end for initializing
 # and a temp variable to help in thw swapping process

def reverse(arr,n):
    start=0
    end=n-1
    temp= 0
    print('Original array : '+str(arr))

    while(start<end):
        #swamp
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start=start + 1
        end=end-1
    print('reversed array : '+str(arr))


arr=[1,2,3,4,5]
n=len(arr)
reverse(arr,n)