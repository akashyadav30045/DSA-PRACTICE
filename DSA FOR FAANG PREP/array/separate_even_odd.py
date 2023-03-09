def getevenodd(l):
    even =[ ]
    odd=[ ]
    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd
#driver code

l = [10,12,11,16]
even , odd =getevenodd(l)
print(even)
print(odd)