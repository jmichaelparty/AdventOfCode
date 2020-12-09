# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:22:51 2020

@author: 00625745
"""


inputData = []

inputFile = open("Day5InputData.txt", "r")
inputData = inputFile.readlines()

class SeatAssignment:
    def __init__(self, seatRow, seatColumn):
        self.row = seatRow
        self.column = seatColumn
        self.id = (seatRow * 8) + seatColumn

def findRow(minRow, maxRow, rowInputString):
    if len(rowInputString) == 1:
        if (rowInputString == "F"):
            x = minRow
        else: 
            x = maxRow
    else:
        if (rowInputString[0] == "F"):
            x = findRow(minRow, int(minRow + ((maxRow - minRow)/2)), rowInputString[1:])
        else: 
            x = findRow(minRow + int((maxRow - minRow + 1)/2), maxRow, rowInputString[1:])
    return x

def findColumn(minCol, maxCol, colInputString):
    if len(colInputString) == 1:
        if (colInputString == "L"):
            y = minCol
        else:
            y = maxCol
    else:
        if (colInputString[0] == "L"):
            y = findColumn(minCol, int(minCol + ((maxCol - minCol)/2)), colInputString[1:])
        else:
            y = findColumn(minCol + int((maxCol - minCol + 1)/2), maxCol, colInputString[1:])
    return y

seatAssignments = []
rowPart = ""
colPart = ""

for line in inputData: 
    rowPart = line[:7]
    colPart = line[7:].strip('\n')
    for i in rowPart:
        if (not (i == "F" or i == "B")):
            print(i, "ERROR")
    for j in colPart:
        if (not (j == "L" or j =="R")):
            print(colPart)
            print(j, "ERROR")
    tempAssignment = SeatAssignment(findRow(0, 127, rowPart), findColumn(0,7, colPart)) 
    seatAssignments.append(tempAssignment)

idSet = set()


for assignment in seatAssignments:
    idSet.add(assignment.id)
    

minSeatID = 0
maxSeatID = (127 * 8) + 7

checkID = 0

for i in range (1, maxSeatID):
    if( (not (i in idSet)) and ((i-1) in idSet) and ((i+1) in idSet)):
        checkId = i

print(checkId)
        
