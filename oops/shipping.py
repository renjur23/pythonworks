class Shipping:
    
    def calculate_shipping(self,weight):
        
        print(weight*5)
        
class ExpreesShipping(Shipping):
    
    def calculate_shipping(self,weight):
        
        print(weight*20)
        
class StandardShipping(Shipping):
    
    def calculate_shipping(self,weight):
        
        print(weight*10)
        
exp_instance=ExpreesShipping()

exp_instance.calculate_shipping(10)

        
exp_instance=StandardShipping()

exp_instance.calculate_shipping(10)
    
    
    

    
    
        
        