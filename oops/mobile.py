class Mobile:
    Name=str
    
    Brand=str
    
    Price=int
    
    def __init__(self,Name,Brand,Price):
        
        self.Name=Name
        
        self.Brand=Brand
        
        self.Price=Price
        
    def display_mobile(self):
        
        print(self.Name,self.Brand,self.Price)
        
Mobile_instance=Mobile("Nord CE 2 5G","OnePlus",24000)

Mobile_instance.display_mobile()