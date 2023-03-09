def linear_search(arr , a):
    for i in range(len(arr)):
        if arr[i] == a :
            return i
    return -1 


#driver code
arr = [20,45,67,98,98,7]
a=67
#function calling
result= linear_search(arr, a)
print("the result of number is " , result)