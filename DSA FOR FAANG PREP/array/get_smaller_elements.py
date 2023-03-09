#python code to print elements in list which are smallaer than the input number

#function code

def smaller_element(l,x):
    b = []   #empty list to store the elements found
    for e in l: #loop to iterate elements across the list
        if e < x:
            b.append(e) #agr  e mera b se chota hoga to vo list me enter kar jayga
    return b #is return ko loop se bahar rkhna h taki aage ki values b le skeee...
    
# driver code
l=[10,20,30,40,50]
x=30
c = smaller_element(l,30)  # function calling
print(c)
    