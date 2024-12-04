class BankAccount:
    
    def __init__(self,name,acc_type,mpin,balance):
        
        self.name=name
        
        self.acc_type=acc_type
        
        self.__mpin=mpin
        
        self.__balance=balance
        
        
    def get_balance(self):
        
        print(self.__balance)
        
    def __str__(self):
        
        return  self.name
    
bank_instance=BankAccount("Hari","Savings",6568,5000)

bank_instance.get_balance()

print(bank_instance.mpin)