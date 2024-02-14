#INSERTION SORT
# example1

# def inser_sort(arr,n):
#     for i in range(1,n):
#         key=arr[i]
#         j=i-1
#         while j>=0 and key <arr[j]:
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=key


# arr=[67,34,32,21,11,2]
# n=len(arr)
# insert=inser_sort(arr,n)
# print("sorted array :" +str(arr))

#example 2

def selc_sort(arr,n):
    for i in range(1,n):
        key=arr[i]

        j=i-1

        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

arrr=[56,34,89,90,76,43,12,21,1]
n=len(arrr)
slsl=selc_sort(arrr,n)
print("sorted array :"+str(arrr))