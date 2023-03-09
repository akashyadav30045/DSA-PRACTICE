#logic 1
def average1(l):
    return sum(l)/len(l)

#logic 2

def average(l):
    sum=0
    i=0
    while i<len(l):
        sum=sum+i
        i=i+1
        return (sum/len(l))

#driver code
l=[10,20,30,40]
output = average(l)
print(output)