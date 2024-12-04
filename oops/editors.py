from abc import ABC,abstractmethod

class Editor(ABC):
    
    @abstractmethod
    
    def open(self):
        
        pass
        
    @abstractmethod
    def write(self):
        
        pass
        
    @abstractmethod
    def debug(self):
        
        pass
        
    @abstractmethod
    def stop(self):
        
        pass
    
class Vscode(Editor):
    
    def open(self):
        
        print("Vscode opened")
        
    def write(self):
        
        print("file wrote")
        
    def debug(self):
        
        print("file debuged")
        
    def stop(self):
        
        print("Vscode stopeed")
        
vscode_instance=Vscode()

vscode_instance.open()

vscode_instance.write()

vscode_instance.debug()

vscode_instance.stop()