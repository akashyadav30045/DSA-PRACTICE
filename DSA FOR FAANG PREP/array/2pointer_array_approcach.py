def two_sum(arr , target_sum):
    l =0
    r=len(arr)-1
    while l<=r:
            if arr[l]+arr[r]== target_sum:
                return(l,r)
            elif arr[l]+arr[r]< target_sum:
                l = l +1
            else:
                r= r -1 
#driver code
arr = [20,40,60,80,90,120,240]
target_sum = 210
result =two_sum(arr , 210)
print(result)