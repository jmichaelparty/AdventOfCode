# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:42:53 2020

@author: 00625745
"""


inputData = []

inputFile = open("Day3InputData.txt", "r")
inputData = inputFile.readlines()

answer1 = 0
answer2 = 0
answer3 = 0
answer4 = 0
answer5 = 0

# First Series
rightMoves = 1
downMoves = 1
countTrees = 0
currentCol = 0
currentRow = 0
for line in inputData: 
    if currentRow % downMoves == 0:
        if line[currentCol] == "#":
            countTrees += 1
        for x in range(0,rightMoves):
            if len(line) > currentCol+2:
                currentCol += 1
            else:
                currentCol = 0
    currentRow += 1
    
answer1 = countTrees


#Second Series
rightMoves = 3
downMoves = 1
countTrees = 0
currentCol = 0
currentRow = 0
for line in inputData:    
    if currentRow % downMoves == 0:
        if line[currentCol] == "#":
            countTrees += 1
        for x in range(0,rightMoves):
            if len(line) > currentCol+2:
                currentCol += 1
            else:
                currentCol = 0
    currentRow += 1
    
answer2 = countTrees

#Third Series
rightMoves = 5
downMoves = 1
countTrees = 0
currentCol = 0
currentRow = 0
for line in inputData:    
    if currentRow % downMoves == 0:
        if line[currentCol] == "#":
            countTrees += 1
        for x in range(0,rightMoves):
            if len(line) > currentCol+2:
                currentCol += 1
            else:
                currentCol = 0
    currentRow += 1

answer3 = countTrees

#Fourth Series
rightMoves = 7
downMoves = 1
countTrees = 0
currentCol = 0
currentRow = 0
for line in inputData:    
    if currentRow % downMoves == 0:
        if line[currentCol] == "#":
            countTrees += 1
        for x in range(0,rightMoves):
            if len(line) > currentCol+2:
                currentCol += 1
            else:
                currentCol = 0
    currentRow += 1
    
answer4 = countTrees

#Fifth Series
rightMoves = 1
downMoves = 2
countTrees = 0
currentCol = 0
currentRow = 0
for line in inputData:    
    if currentRow % downMoves == 0:
        if line[currentCol] == "#":
            countTrees += 1
        for x in range(0,rightMoves):
            if len(line) > currentCol+2:
                currentCol += 1
            else:
                currentCol = 0
    currentRow += 1
    
answer5 = countTrees

print(answer1 * answer2 * answer3 * answer4 * answer5)

