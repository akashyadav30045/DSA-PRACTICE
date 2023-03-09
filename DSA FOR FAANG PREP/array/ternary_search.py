# 09 03 2023 00:03
#ternary search
#writing function
def ternary_search (arr,i,j,target):
    
    while i<=j:
        mid1=i+(j-i)//3
        mid2=j-(j-i)//3
        if (arr[mid1]==target):
            return mid1
        elif (arr[mid2]==target):
            return mid2
        elif (target<arr[mid1]):
            return ternary_search(arr,i, mid1-1,target)
        elif (target>arr[mid2]):
            return ternary_search(arr,mid2+1,j,target)
        else:
            return ternary_search(arr,mid1+1,mid2-1,target)
    return -1

#driver code
arr = [20,25,47,56,59,63,65,79,82] #in sorted manner
i=0
j=len(arr)-1
target = 47

result = ternary_search(arr,i,j,target)
print(result)