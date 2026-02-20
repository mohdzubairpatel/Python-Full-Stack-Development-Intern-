class Account:
    
    def __init__(self, balance, Acc_no):
        self.balance = balance
        self.Acc_no = Acc_no

    # @staticmethod
    def debit(self, amount):
        self.balance -= amount
        print(f"The Amount Debited from account no. {self.Acc_no} is {amount}")
        print(f"Total balace is {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"The Amount credited to account no. {self.Acc_no} is {amount}")
        print(f"Total balace is {self.balance}") 


acc1 = Account(10000,20200143)
acc1.debit(1000)
acc1.credit(3000)
print("---------------------------------------------")
acc2 = Account(20000,20200144)
acc1.debit(1000)
acc1.credit(3000)

