# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:13:10 2020

@author: 00625745
"""


inputData = []

inputFile = open("Day1InputData.txt", "r")


#contents = inputFile.read()
#
#print(contents)

inputData = inputFile.readlines()
inputData2 = inputData
inputData3 = inputData
a = 0
b = 0

for line in inputData:
    for line2 in inputData2:
        for line3 in inputData3:
            a = int(line) + int(line2) + int(line3)
            if a == 2020: 
                b = int(line) * int(line2) * int(line3)
                print("1: ", int(line), ", 2: ", int(line2), " 3: ", int(line3), " Product = ", b)
        

inputFile.close()