#selection sort
#function defining
#time_complexity O(n^2)
def selection_sort(arr):
    n=len(arr)
    for i in range(n): #i will run through length of aray
        min_idx=i #minimum index value is i fisrt value
        for j in range(i+1,n):
#i+1 is taken bcoz it compares the value of i with next element
#suppose there are 2 elements one is 1,2 i is 1 and i+1=2 so it start comparing with i+1
            if arr[j]<arr[min_idx] :
                min_idx=j
#swap happened after every pass
            arr[i], arr[min_idx] = arr[min_idx],  arr[i]
    return arr
#driver code
arr = [10,9,8,7,15,16]
result=selection_sort(arr)
print("the sorted array is",result)