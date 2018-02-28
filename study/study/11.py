'''
Created on 05-Jan-2018

@author: samir
'''

class circle:
    
    def __init__(self, redius="0"):
        self.redius = redius
        
    
    @property
    def redius(self):
        print("In Getter")
        return self.__redius
    
    @redius.setter
    def redius(self, value1):
        print("In Setter")
        self.__redius = value1
    def getarea(self):
        area = 3.14 * self.__redius * self.__redius
        return area
        
        
   
def main():
    
    aCircle = circle
    redius = int(input("Enter the redius : "))
    aCircle.redius = redius
    print("Set value")
    print("Area of circle is :", aCircle.getarea())
    

main()