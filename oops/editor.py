class Editor:
    
    name=str
    
    vendor=str
    
    def __init__(self,name,vendor):
        
        self.name=name
        
        self.vendor=vendor
        
    def __str__(self):
        
        return self.name
    
    
editor_instance=Editor("pycharam","jebrains")

print(editor_instance)
        