'''
Created on 02-Jan-2018

@author: samir
'''
import os
 
with open("myfile.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("random text \n more random text \n some more random function")

with open("myfile.txt",encoding="utf-8") as myFile:
    linenum = 1
    
    while True:
        line = myFile.readline()
        
        if not line:
            break
        print("Line", linenum, ":", line)
        wordList = line.split()
        print("Number of words : ", len(wordList))
        linenum += 1





 
 
 
# 
# print(myFile.mode)
# 
# with open("myfile.txt",encoding="utf-8") as myFile:
#     
#     print(myFile.readlines())
# 
# print(myFile.closed)
# 
# print(myFile.name)
# 
# print(myFile.mode)
# 
# print(os.getcwd())

# number = int(input("How many number you want to print in fab series :"))
# 
# first_num = 0
# second_num = 1
# 
# count = 2
# print(first_num)
# print(second_num)
# 
# while(count != number):
#     next_num = int(first_num + second_num )
#     print(next_num)
#     first_num = second_num
#     second_num = next_num
#     count+=1

    