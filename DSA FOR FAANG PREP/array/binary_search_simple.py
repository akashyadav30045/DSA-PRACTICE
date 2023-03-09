#function defining
def binarysearch (arr,x,firstindex,lastindex):
    while firstindex <=lastindex :
        mid = firstindex+(lastindex-1)//2
        if arr[mid] ==x:
            return mid
        elif arr[mid]<x:
            firstindex=mid+1
        else:
            lastindex=mid-1  
        
#driver code
arr = [20,30,40,50,60,70,90]
x=60
firstindex=0
lastindex=len(arr)-1
#function call
result=binarysearch(arr,x,firstindex,lastindex)
print("the result of the number is " , result)