def power_of_element(a,n):
    #small problem
    if n==1:
        return a
    if n==0:
        return 1
# 1 . Divide
    mid=n//2
# 2 . conquer 
    b=power_of_element(a,mid)
    result=b*b
# 3 . combine
#here checking for odd and even
    if n%2==0:
        return result
    else:
        return result*a

#driver code
a=5
n= 12
result = power_of_element(a,n)
print("the result of number is" , result)

print(5**12)