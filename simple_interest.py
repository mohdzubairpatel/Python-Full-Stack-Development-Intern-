Amount = int(input("enter the amount you give: "))
Time = int(input("enter the the years: "))
Rate = int(input("enter the Rate of interest at which the Amount is given: "))

def Simple_interest(x,y,z):
    Simple_interest_price = (x*y*z)/100
    print(f"simple interest is {Simple_interest_price}")


Simple_interest(Amount,Time,Rate)