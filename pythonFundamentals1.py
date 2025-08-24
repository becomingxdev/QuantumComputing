#API responses would be in form of json files. We are learning two important data structures. Lists and Dictionaries

#Starting with lists
bobBases = ['x', 'z', 'x', 'x', 'x', 'z', 'z', 'z']
bobResult = [0, 1, 1, 1, 0, 0, 0, 1]
bit_string = "10110"
bitList = [int(i) for i in bit_string]




#Dictionaries
keyExchangeStatus = {
    "key" : "1011001",
    "eavesDropperDetected" : False,
    "errorRate" : 0.02
}

countOf0 = 0
countOf1 = 0
countOfError = 0
for i in bitList:
    if(i == 0):
        countOf0 += 1
    elif(i == 1):
        countOf1 += 1
    else:
        countOfError += 1

results = {
    "0" : countOf0,
    "1" : countOf1,
    "error" : countOfError
}