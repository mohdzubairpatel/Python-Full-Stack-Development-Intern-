Amount = int(input("enter the cost of the food you purchased"))
gst = int(input(" % of gst got the purchased product"))

def food_order(x,y):
    total_amount = x + (y/100)*Amount

    print("Total amount for the purchased product is:", total_amount)


food_order(Amount,gst)