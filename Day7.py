# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:10:45 2020

@author: 00625745
"""

inputData = []

inputFile = open("Day7InputData.txt", "r")
inputData = inputFile.readlines()

myBagColor = "shiny gold"

finalSet = set()

def findChildren(bagColor):
    x = []
    for line in inputData:
        tempBagColor = (line.split("bags")[0]).rstrip(" ")
        if tempBagColor == bagColor: 
            if line.count(",") < 1:
                if line.count("no other") >0:
                    x.clear()
                else: 
                    right1 = (line.split("contain")[1].lstrip(" ")).rstrip(" ")
                    numBags = right1.split(" ")[0]
                    childBagColor = (((right1.split("bag")[0]).split(numBags)[1]).lstrip(" ")).rstrip(" ")
                    x.append(childBagColor)
                    tempChildren = []
                    tempChildren = findChildren(childBagColor)
                    for j in tempChildren:
                        x.append(j)
            else:
                right1 = (line.split("contain")[1].lstrip(" ")).rstrip(" ")
                for i in right1.split(","):
                    temp = i.lstrip(" ")
                    numBags = temp.split(" ")[0]
                    childBagColor = (((temp.split("bag")[0]).split(numBags)[1]).lstrip(" ")).rstrip(" ")
                    x.append(childBagColor)
                    tempChildren = []
                    tempChildren = findChildren(childBagColor)
                    for j in tempChildren:
                        x.append(j)
    return x

def findNumBags(bagColor):
    x = 0
    for line in inputData:
        tempBagColor = (line.split("bags")[0]).rstrip(" ")
        if tempBagColor == bagColor: 
            if line.count(",") < 1:
                if line.count("no other") > 0:
                    x = x + 0
                else: 
                    right1 = (line.split("contain")[1].lstrip(" ")).rstrip(" ")
                    numBags = right1.split(" ")[0]
                    childBagColor = (((right1.split("bag")[0]).split(numBags)[1]).lstrip(" ")).rstrip(" ")
                    x = x + int(numBags)
                    x = x + int(numBags)*(findNumBags(childBagColor))
            else:
                right1 = (line.split("contain")[1].lstrip(" ")).rstrip(" ")
                for i in right1.split(","):
                    temp = i.lstrip(" ")
                    numBags = temp.split(" ")[0]
                    childBagColor = (((temp.split("bag")[0]).split(numBags)[1]).lstrip(" ")).rstrip(" ")
                    x = x + int(numBags)
                    x = x + int(numBags)*(findNumBags(childBagColor))
    return x

print(findNumBags(myBagColor))

# ====                Part 1
# =============================================================================
# children = []
# count = 0
# for line in inputData:
#     currentBagColor = (line.split("bags")[0]).rstrip(" ")
#     print("Current Color: ", currentBagColor)
#     children = findChildren(currentBagColor)
#     print("All children: ", children)
#     if myBagColor in children:
#         print("VERIFIED: ", currentBagColor)
#         count += 1
# print(count)
# =============================================================================

