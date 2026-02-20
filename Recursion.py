n = int(input("enter the number of times need to print:--> "))
name = input("enter the name need to print:-->")

def print_name(x,y):
    if x == 0 :
        return
    
    else:
        print(y, end=" ")
        print_name(x -1 , y)

print_name(n, name)