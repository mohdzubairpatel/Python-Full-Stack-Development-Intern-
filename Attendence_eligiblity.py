days =[]
for i in range(1,7+1):
    day = int(input(f"enter the attendence ofr day {i} :"))

    if day == 0 or day == 1:
        days.append(day)
    
    else:
        print("enter 0 or 1 incorrect input")
        break

total_attendence = sum(days)
print(total_attendence)

if total_attendence >= 4:
    print("eligible for exam")

else:
    print("not eligible for exam")

