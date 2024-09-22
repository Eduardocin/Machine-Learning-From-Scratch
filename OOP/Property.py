class Rectangle:  
    def __init__(self, width, height):  
        self._width = width  
        self._height = height  
    
    @property  
    def area(self):  
        return self._width * self._height  # Corrigido: usar _height  
    
    @property  
    def width(self):  
        return self._width  
    
    @width.setter  
    def width(self, value):  
        if value < 0:  
            raise ValueError("Width must be a positive number")  
        self._width = value  
    
    @property  
    def height(self):  # Adição do getter para height  
        return self._height  

    @height.setter  
    def height(self, value):  
        if value < 0:  
            raise ValueError("Height must be a positive number")  
        self._height = value  
        
    @height.deleter  
    def height(self):  
        del self._height  
        print("Height has been removed")  
        

# Criando uma instância de Rectangle  
rectangle = Rectangle(3, 4)  
print(rectangle.area)  # Output: 12  

rectangle.width = 5  
print(rectangle.width)  # Output: 5  

# Deletando a altura   
del rectangle.height  
#print(rectangle.height)  # Isto causaria um erro agora, porque height foi deletado