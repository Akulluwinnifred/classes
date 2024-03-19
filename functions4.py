def vat(rate,price):
    frate = (rate / 100) * price
    return frate #return exposes a value to any function
    #print(int(frate))
#vat(18,20000)


def actualprice():
    actualvat = vat(18,20000)
    netprice = actualvat + 20000
    print(netprice)
actualprice()


#return is the last statement to be executed in a function



#using parameterized functions,create three functions which shares one anothers values and print the last







def discount(price,discount_percentage):
    discount = discount_percentage /  100 * price
    return discount
    print(int(discount))
discount(50000,20)


def discounted_pay(discount,price):
    discount = discount(20,50000)
    discounted_price = 50000 - discount
    return discounted_price
    print(int(discounted_price))
discounted_pay(discount,50000)


vat = 3500
def totalpay():
    total = vat + discounted_pay(discount,50000)
    print(total)
totalpay()


