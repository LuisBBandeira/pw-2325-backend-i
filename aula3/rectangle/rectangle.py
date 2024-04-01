class Rectangle:

    def __init__(self , width:int ,height:int ):
        self.width = width
        self.height = height
    
    def get_area(self)->int:
        return self.width*self.height
    
    def get_perimeter(self)->int:
        return (self.width*2)+(self.height*2)