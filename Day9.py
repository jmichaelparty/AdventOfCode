# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 07:54:39 2020

@author: 00625745
"""


inputData = []
inputFile = open("Day9InputData.txt", "r")
inputData = inputFile.readlines()
inputDataIntList = []

preambleLength = 25

for line in inputData:
    inputDataIntList.append(int(line))

def checkXMAS(inputArray, index, preamble):
    possibleOutcomes = []
    for i in range(index - preamble, index):
        x = inputArray[i]
        for j in range (index - preamble + 1, index):
            y = inputArray[j]
            if (not (i == j)):
                possibleOutcomes.append(x + y)
    return possibleOutcomes

def findWeakness(inputArray, checkNumber):
    valuesSet = set()
    for i in range(0, len(inputArray)):
        valuesSet.clear()
        rollingSum = 0
        j = i + 1
        rollingSum = inputArray[i]
        valuesSet.add(int(inputArray[i]))
        while rollingSum < checkNumber:
            rollingSum += inputArray[j]
            valuesSet.add(int(inputArray[j]))
            if rollingSum == checkNumber:
                return valuesSet
            j += 1

k = 0
badCheck = 0
for checkNumber in inputDataIntList:
    if k >= preambleLength:
        if not (checkNumber in checkXMAS(inputDataIntList, k, preambleLength)):
            if badCheck == 0:
                badCheck = (checkNumber)
    k +=1

resultSet = set()
resultSet = findWeakness(inputDataIntList, badCheck)
print("Bad Value: ", badCheck)
print(resultSet)
minVal = min(resultSet)
maxVal = max(resultSet)
print("Min: ", minVal)
print("Max: ", maxVal)
print("Sum: ", minVal + maxVal)