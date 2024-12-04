class Car:
    
    name=str
    
    brand=str
    
    fuel_type=str
    
    
    def __init__(self,name,brand,fuel_type):
        
        self.name=name
        
        self.brand=brand
        
        self.fuel_type=fuel_type
        
    def dispaly_car(self):
        
        print(self.name,self.brand,self.fuel_type)
        
    def __str__(self):
        
        return self.name
        
        
car_instance=Car("Swift","Suzuki","Petrol")

car_instance.dispaly_car()

print(car_instance)