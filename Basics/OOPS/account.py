class Account:
    def __init__(self,balance):
        self.balance = balance
    def getbalance(self):
        print(f"the current balance is: {self.balance:.2f}")
    def credit(self,amt):
        self.balance+=amt
        self.getbalance()
    def debit(self,amt):
        if(amt>self.balance):
            print("unable to debit money!!, you balance is low!!!!")
        else:
            print(f"Amount {amt:.1f} debited sucessfully")
            self.balance-=amt
user1 = Account(540021.42)
user1.debit(600000.00)
user1.getbalance()