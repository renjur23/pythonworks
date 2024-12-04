class Parent:
    
    def mobile(self):
        
        print("Nokia")
        
    def vehicle(self):
        
        print("Hunter")
        
class Child(Parent):
    
   def mobile(self):
        
        print("Nokia")
        
   def vehicle(self):
        
        print("Hunter")
        
child_instance=Child()

child_instance.mobile()
        
