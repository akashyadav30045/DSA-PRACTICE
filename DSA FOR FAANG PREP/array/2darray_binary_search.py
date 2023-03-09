#date - 8-03-2023 time 22:09 course- ineuron

#def function
import math as mt
def search_2d_binary(arr,target):
    #first step - take the no of rows
    m = len(arr) #this takes length of row elements
    if m ==0:
        return False
    #now we defien no of columns
    n=len(arr[0])
    left , right=0 , m*n-1
    #Binary search implementation 
    while left<=right:
        mid=left + (right-left)//2
        #this defines the index of elements which contains the middle elements
        #n is the no of columns present
        #arr is represented as arr[row][column]
        mid_element = arr[mid//n][mid%n]
        if target == mid_element:
            return True
        elif target < mid_element:
            right = mid - 1
        else :
            left = mid+  1
    return False

#driver code
arr = [[1,3,5,7],[10,11,16,20],[23,30,24,60]]
target=9
result = search_2d_binary(arr , target)
print(result)
