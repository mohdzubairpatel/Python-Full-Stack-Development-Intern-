def tea_vending_machine():
    yield "1 cup of tea is reay"
    yield "2 cup of tea is reay"
    yield "3 cup of tea is reay"
    yield "4 cup of tea is reay"



tea = tea_vending_machine()

for i in tea:
    print(i)