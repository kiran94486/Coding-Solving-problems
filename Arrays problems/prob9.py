#MERGE SORT IN PYTHON


# def merge_sort(arr, n):
#     if n > 1:
#         mid = n // 2
#         L = arr[:mid]
#         R = arr[mid:]
#         merge_sort(L, len(L))
#         merge_sort(R, len(R))
#         i = j = k = 0
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1


# def printarr(arr, n):
#     for i in range(n):
#         print(arr[i], end=", ")
#     print()


# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     n = len(arr)
#     print("Given array is")
#     printarr(arr, n)
#     merge_sort(arr, n)
#     print("\nSorted array is ")
#     printarr(arr, n)




#Example x

def mergg(arry):
    if len(arry)>1:
        mid=len(arry)//2

        L=arry[:mid]
        R=arry[mid:]
        
        mergg(L)
        mergg(R)




        i=j=k=0
        while(i<len(L) and j<len(R)):
            if L[i]<=R[j]:
                arry[k]=L[i]
                i=i+1
            else:
                arry[k]=R[j]
                j=j+1
            k=k+1

        while(i<len(L)):
            arry[k]=L[i]
            i=i+1
            k=k+1

        while(j<len(R)):
            arry[k]=R[j]
            j=j+1
            k=k+1

    return arry


arry = [12, 11, 13, 5, 6, 7]

mery=mergg(arry)
print('Sorted array :'+str(mery))