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
