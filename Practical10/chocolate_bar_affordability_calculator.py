def afford(x,y):
    """
    Input:x,the total money;y,the price of one chocolate bar
    divide x by y
    get and return the quotient ande the reiminder
    """
    x=int(x)
    y=int(y)
    q=x//y
    r=x%y
    op="You can by "+str(q)+" bar(s) of chocolate."+"\n"+"Change: "+str(r)
    print(op)
    return op
a=input("Total money: ")
b=input("The price of one chocolate bar: ")
afford(a,b)
    
