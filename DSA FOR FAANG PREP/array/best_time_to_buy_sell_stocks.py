def findmaxprofit(price):
    minprice = float('inf')
    maxprofit= 0
    for i in range(len(price)):
        if price[i]<minprice:
            minprice=price[i]
        elif price[i] - minprice >maxprofit:
            maxprofit=price[i]-minprice
    return maxprofit
        
#drivercode
price = [7,1,5,3,6,4]
maxprofit_value =  findmaxprofit(price)
print("the max profit of buying and selling is " ,maxprofit_value)