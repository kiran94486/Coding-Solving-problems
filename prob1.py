#Find a peak element which is not smaller than its neighbours
# Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the maximum element in the array.

# Note: If the array is increasing then just print the last element will be the maximum value.

# Example:

# Input: array[]= {5, 10, 20, 15}
# Output: 20
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.



def test_run(arr,n):
    if n==1:
        return 0
    if arr[0] >= arr[1]:
        return 0
    if arr[n-1] >= arr[n-2]:
        return n-1
    
    for i in range(1,n-1):
        
        if arr[i] >= arr[i-1] and arr[i-1] >= arr[i-2]:
            return i
        




arr = [5,10,20,15]
n=len(arr)
print("Index of a peak point is",test_run(arr,n))

# Time complexity: O(n), One traversal is needed so the time complexity is O(n)
# Auxiliary Space: O(1), No extra space is needed, so space complexity is constant
