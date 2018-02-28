'''
Created on 05-Jan-2018

@author: samir
'''
# 
# class Dog:
#     
#     def __init__(self, name="", hight=0, weight=0):
#         self.name = name
#         self.height = hight
#         self.weight = weight
#     
#     def Run(self):
#         print("{} is running ".format(self.name))
#     
#     def height(self):
#         print("The height of the dog is {}".format(self.height))
#         
# 
# def main():
#     
#     Doggy = Dog("Doggy",20,30)
#     Doggy.Run()
#    
#     
#     
# main()
from builtins import int

class Square:
    
    def __init__(self,height="0", width="0"):
        self.height = height
        self.width = width
    
    
    @property
    def height(self):
        print("Retrieving Height")
        return self.__height
    
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please enter number")
    
    
    @property
    def width(self):
        print("Retrieving width")
        return self.__width
    
    @width.setter
    def width(self, value):
        
        if value.isdigit():
            self.__width = value
        else:
            print("Enter number for width")
    
    def getArea(self):
        
        return int(self.__height) * int(self.__width)  

def main():
    aSqure = Square()
    height = input("Enter Height :")
    width = input("Enter Width :")
    
    aSqure.height = height
    aSqure.width = width
    
    print("Height is : ", aSqure.height)
    print("Width is :", aSqure.width)
    
    print("Area of Square  : ", aSqure.getArea())
    
main() 
    
    
    
    
    
    
    