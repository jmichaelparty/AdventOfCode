# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:50:14 2020

@author: 00625745
"""


inputData = []

inputFile = open("Day4InputData.txt", "r")
inputData = inputFile.readlines()

passports = []

class Passport:
    def __init__(self, birthyear, issueyear, expirationyear, height, haircolor, eyecolor, passportid, countryid):
        self.byr = birthyear
        self.iyr = issueyear
        self.eyr = expirationyear
        self.hgt = height
        self.hcl = haircolor
        self.ecl = eyecolor
        self.pid = passportid
        self.cid = countryid
        
byrTemp = ""
iyrTemp = ""
eyrTemp = ""
hgtTemp = ""
hclTemp = ""
eclTemp = ""
pidTemp = ""
cidTemp = ""

checkPassport = False
validPassports = 0

for line in inputData: 
    if line == "\n":
        if(checkPassport):
            tempPassport = Passport(byrTemp, iyrTemp, eyrTemp, hgtTemp, hclTemp, eclTemp, pidTemp, cidTemp)
            passports.append(tempPassport)
        byrTemp = ""
        iyrTemp = ""
        eyrTemp = ""
        hgtTemp = ""
        hclTemp = ""
        eclTemp = ""
        pidTemp = ""
        cidTemp = ""
        checkPassport = False
    else:
        checkPassport = True
        for statement in line.split(" "):
            x = statement.split(":")
            if (x != ""): 
                key = x[0]
                value = x[1].strip('\n')
                if(key == "byr"):
                    byrTemp = value
                if(key == "iyr"): 
                    iyrTemp = value
                if (key == "eyr"):
                    eyrTemp = value
                if (key == "hgt"):
                    hgtTemp = value
                if (key == "hcl"):
                    hclTemp = value
                if (key == "ecl"):
                    eclTemp = value
                if (key == "pid"):
                    pidTemp = value
                if (key == "cid"):
                    cidTemp = value
if(checkPassport):
    tempPassport = Passport(byrTemp, iyrTemp, eyrTemp, hgtTemp, hclTemp, eclTemp, pidTemp, cidTemp)
    passports.append(tempPassport)
            
for p in passports:
    byrCheck = False
    iyrCheck = False
    eyrCheck = False
    hgtCheck = False
    hgtVal = ""
    hclCheck = False
    eclCheck = False
    pidCheck = False
    
    if (len(p.byr) == 4 and (p.byr).isdigit() and int(p.byr) >= 1920 and int(p.byr) <= 2002):
        byrCheck = True
    if (len(p.iyr) == 4 and (p.iyr).isdigit() and int(p.iyr) >= 2010 and int(p.iyr) <= 2020):
        iyrCheck = True
    if (len(p.eyr) == 4 and (p.eyr).isdigit() and int(p.eyr) >= 2020 and int(p.eyr) <= 2030):
        eyrCheck = True
    if ((p.hgt).endswith("in") or (p.hgt).endswith("cm")):
        hgtVal = (p.hgt[:-2])
        if( (p.hgt).endswith("in") and int(hgtVal) >= 59 and int(hgtVal) <= 76):
            hgtCheck = True
        if( (p.hgt).endswith("cm") and int(hgtVal) >= 150 and int(hgtVal) <= 193):
            hgtCheck = True
    if(len(p.hcl) == 7 and p.hcl[0] == '#'):
        hclCheck = True
        for i in range(1,6):
            if (not (p.hcl[i].isdigit() or (ord(p.hcl[i]) >= 97 and ord(p.hcl[i]) <= 102)) ):
                hclCheck = False
    if(p.ecl == "amb" or p.ecl == "blu" or p.ecl == "brn" or p.ecl == "gry" or p.ecl == "grn" or p.ecl == "hzl" or p.ecl == "oth"):
        eclCheck = True
    if(len(p.pid) == 9 and (p.pid).isdigit()):
        pidCheck = True
    
    print("Passport")
    print("byr: ", p.byr)
    print("iyr: ", p.iyr)
    print("eyr: ", p.eyr)
    print("hgt: ", p.hgt, "hgtVal: ", hgtVal)
    print("hcl: ", p.hcl)
    print("ecl: ", p.ecl)
    print("pid: ", p.pid)
    print("cid: ", p.cid)
    if(p.byr != "" and p.iyr !="" and p.eyr !="" and p.hgt != "" and p.hcl != "" and p.ecl != "" and p.pid != "" and byrCheck and iyrCheck and eyrCheck and hgtCheck and hclCheck and eclCheck and pidCheck):
        print("VALID")
        validPassports += 1
    else:
        print("INVALID")
    
print(validPassports)