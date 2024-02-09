class test:
    def test_run(arr,n):
        if n==1:
            return 0
        if arr[0] >= arr[1]:
            return 0
        if arr[n-1] >= arr[n-2]:
            return n-1
        
        for i in range(1,n-1):
            













arr = [5,10,20,15]
n=len(arr)
print("Index of a peak point is",test_run(arr,n))
