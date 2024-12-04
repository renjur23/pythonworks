class Animal:
    
    name=str
    sound=str
    
    def set_animal(self,name,sound):
       
       self.name=name
       self.sound=sound
       
    def sound_animal(self):
        
        print(f"sound of",self.name, "is",self.sound)
        

lion_instance=Animal()

cat_instance=Animal()

lion_instance.set_animal("Lion","roar")

cat_instance.set_animal("Cat","meow")

lion_instance.sound_animal()

cat_instance.sound_animal()