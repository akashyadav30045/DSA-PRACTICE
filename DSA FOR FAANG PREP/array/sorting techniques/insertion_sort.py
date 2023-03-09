#insertion sort 
def insertion_sort(arr):
    for i in range (1,len(arr)): #we will iterate i till len -1
        j= i- 1 #j ki value i ke ek element chordne k bd li jayegi
        key=arr[i] #1st element is taken as key 
        while j>=0 and arr[j]>key: #it compares the value of j till index 0
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1] = key
    return arr
    
    
    
    #driver code
arr=[75,90,100,95,85,80]
sort=insertion_sort(arr)
print(sort)