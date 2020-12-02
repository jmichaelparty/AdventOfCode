# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:34:48 2020

@author: 00625745
"""


inputData = []

inputFile = open("Day2InputData.txt", "r")
inputData = inputFile.readlines()
validPasswords1 = 0
validPasswords2 = 0


for line in inputData:
    policy,password = line.split(':')
    policyMin,policyRight2 = policy.split('-')
    policyMax,policyLetter = policyRight2.split(' ')
    letterCount = 0
    for i in password:
        if i == policyLetter:
            letterCount += 1 
    #print("Password: ", password, ". Key: ", policyLetter, " - Count: ", letterCount)
    if letterCount >= int(policyMin) and letterCount <= int(policyMax):
        validPasswords1 += 1
    
for line in inputData:
    policy,password = line.split(':')
    position1,policyRight2 = policy.split('-')
    position2,policyLetter = policyRight2.split(' ')
    password = password.lstrip()
    
    if password[int(position1) -1] == policyLetter or password[int(position2) -1] == policyLetter:
        if not(password[int(position1) -1] == policyLetter and password[int(position2) -1] == policyLetter):
            validPasswords2 += 1
        
print("Valid Passwords - Problem 1: ", validPasswords1)
print("Valid Passwords - Problem 2: ", validPasswords2)

