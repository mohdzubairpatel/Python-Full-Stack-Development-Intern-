n = int(input("enter the number:--> "))

def sum_of_n(x):
    if x == 0:
        return 0
    else:
        return x  + sum_of_n(x-1)


total_sum = sum_of_n(n)
print(f"total sum:--> {total_sum}")
