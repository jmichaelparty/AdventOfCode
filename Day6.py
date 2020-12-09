# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:13:57 2020

@author: 00625745
"""


inputData = []

inputFile = open("Day6InputData.txt", "r")
inputData = inputFile.readlines()

listOfSets = []

newGroup = True
groupSet = set()
tempGroupSet = set()
tempPersonSet = []
tempGroupList = []
groupList = []


for line in inputData:
    if (line == "\n"):
        newGroup = True
        groupList.append(list(tempGroupList))
        tempGroupList.clear()
        tempGroupSet.clear()
    else:
        tempPersonSet.clear()
        for x in line.strip('\n'):
            tempPersonSet.append(x)
        tempGroupList.append(set(tempPersonSet))

groupList.append(tempGroupList)

count = 0
for i in groupList:
    if len(i) == 1:
        for j in i:
            count += len(j)
    if (len(i) > 1):
        index = 0
        tempIntersect = set()
        tempIntersect.clear()
        for j in i:
            if (index == 0):
                tempIntersect = j
            else:
                tempIntersect = set.intersection(tempIntersect, j)
            index += 1
        count += len(tempIntersect)    
print(count)
    