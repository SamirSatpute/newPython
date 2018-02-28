'''
Created on 08-Feb-2018

@author: samir
'''

class Dog:
    '''
    classdocs
    '''


    def __init__(self, name="", weight=0, height=0):
        '''
        Constructor
        '''
        self.name = name
        self.weight = weight
        self.height = height
        
    def run(self):
        print("{} the dog run".format(self.name))
        
    def height(self):
        print("The hieght of dog is {}".format(self.height))
        
    def weight(self):
        print("The weight of dog is {}".format(self.weight))

def main():
    
    obj = Dog("Kutti", 25, 15)
    obj.run()
    
 
    
main()    