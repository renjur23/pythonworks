class Bank:
    acc_no=int
    
    balance=int
    
    acc_type=str
    
    customer_name=str
    
    def __init__(self,acc_no,balance,acc_type,customer_name):
        
        self.acc_no=acc_no
        
        self.balance=balance
        
        self.acc_type=acc_type
        
        self.customer_name=customer_name
        
    def deposit(self,amount):
        
        self.balance+=amount
        
        print(f"{self.customer_name},your account {self.acc_no} is credited with {amount},your available is {self.balance}")
    
    def withdraw(self,amount):
        
        if self.balance>=amount:
        
          self.balance-=amount
        
          print(f"{self.customer_name},your account {self.acc_no} is debited with {amount},your available is {self.balance}")
          
        else:
            
            print(f"insuffient balance{self.balance}")
            
    def get_balance(self):
        
        print(f"{self.customer_name},your account {self.acc_no}your available is {self.balance}")
        
bank_instance=Bank(9998010270991,100000,"savings","Renjith")

bank_instance.deposit(50000)

bank_instance.withdraw(5000)

bank_instance.get_balance()
        
