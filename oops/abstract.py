from abc import ABC,abstractmethod

class Bike(ABC):
    
    @abstractmethod
    def start(self):
        
        pass
    
    @abstractmethod
    def accelerator(self):
        
        pass
    
    @abstractmethod
    def stop(self):
        
        pass
    
class Hunter(Bike):
    
    def start(self):
        
        print("Hunter staretd")
        
    def accelerator(self):
        
        print("Hunter accelerated")
        
    def stop(self):
        
        print("Hunter stopped")
        
hunter_instance=Hunter()

hunter_instance.start()

hunter_instance.accelerator()

hunter_instance.stop()