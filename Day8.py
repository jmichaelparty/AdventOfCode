# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:02:19 2020

@author: 00625745
"""


inputData = []
inputFile = open("Day8InputData.txt", "r")
inputData = inputFile.readlines()
executedLines = []

def testCode(checkFile):
    checkVar = True 
    success = False
    accumulator = 0
    index = 0
    executedLines.clear()
    while checkVar:
        line = checkFile[index]
        command = line.split(" ")[0]
        valueSign = ((line.split(" ")[1]).lstrip(" "))[0]
        value = (line.split(" ")[1])[1:]
        if command == "acc":
            if valueSign == "+":
                accumulator += int(value)
                executedLines.append(index)
                index +=1
            else:
                accumulator -= int(value)
                executedLines.append(index)
                index +=1
        if command == "jmp":
            executedLines.append(index)
            if valueSign == "+":
                index += int(value)
            else: 
                index -= int(value)
        if command == "nop":
            executedLines.append(index)
            index +=1
            
        if index in executedLines:
            checkVar = False
            return None
        if index == len(checkFile)-1:
            checkVar = False
            success = True
    if success:
        line = checkFile[index]
        command = line.split(" ")[0]
        valueSign = ((line.split(" ")[1]).lstrip(" "))[0]
        value = (line.split(" ")[1])[1:]
        if command == "acc":
            if valueSign == "+":
                accumulator += int(value)
            else:
                accumulator -= int(value)
        return accumulator

tempData = []

for i in range(0,len(inputData)):
    tempData = inputData.copy()
    line = tempData[i]
    command = line.split(" ")[0]
    valueSign = ((line.split(" ")[1]).lstrip(" "))[0]
    value = (line.split(" ")[1])[1:]
    if command == "jmp":
        tempData[i] = tempData[i].replace("jmp","nop")
    if command == "nop":
        tempData[i] = tempData[i].replace("nop","jmp")
    if (not (testCode(tempData)) == None):
        print(testCode(tempData))
