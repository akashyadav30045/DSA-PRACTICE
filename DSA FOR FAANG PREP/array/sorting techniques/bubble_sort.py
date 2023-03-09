#bubble sort
#time complexty O(n^2) as we r using nested for loops:
def bubble(arr):
    n=len(arr)
    for i in range(n):
            for j in range(0,n-i-1):
#(n-i-1) is used as logic bcoz we r reducing one element one by one for ex : in this case 
#the 40 reaches at end , and the comparison end before 40 leaving it 
#than again when another element reachees 40 its skips end 2 numbers 
#for eg in 1st n=5terms i=0 j= 5-0-1=4 when i =0 j=4-0-1=3 than loop will iterate to 0 to 3 index.
                if arr[j]>arr[j+1]:
            #swap the elements
                        arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr             
#driver code
arr = [20,10,30,40,12]
result= bubble(arr)
print(result)
