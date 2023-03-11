#defining function.
#recurance relation time complexity is O(N)
def find_max_and_min (arr,i,j):
    #case1 for 1 elements
    if i==j:
        max_val=arr[i]
        min_val=arr[i]
#case 2 for 2 elements
    elif i == j-1:
#let 20,10 2 elements i = 0index and 20 , j=1 index and 10
# j=1 j-1 =0 and i=0 so this is comapring both
        if arr[i]<arr[j]:
            max_val=arr[j]
            min_val=arr[i]
        else:
            max_val=arr[i]
            min_val=arr[i]
            #Divide and conquer approach
#1         divide approach now when n>2
    else:
        mid = i+ (j-i)//2
# 2          recrusion now
        max1,min1 = find_max_and_min(arr,i, mid)
        max2,min2 = find_max_and_min(arr, mid+1,j)
        
        if(min1<min2):
            min_val= min1
        else:
            min_val=min2
        if(max1<max2):
            max_val=max2
        else:
            max_val=max1
    return min_val,max_val
#driver code

arr =[10,20,15,12,60,80,90]
#starting index
i=0
#end index
j=len(arr)-1
min_val ,max_val =find_max_and_min (arr ,i,j)
print("the minium value is " , min_val ,max_val)