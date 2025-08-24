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




#Learning def function of python.
import random
def generateBits(lenght):
    """ This program genrates bits of given length."""
    bitsList = [random.randint(0, 1) for i in range(lenght)]
    return bitsList
print(generateBits(8))




#OOP Concept in python
class Communicator:
    def __init__(self, name):
        self.name = name
        self.bits = []

    def genrateBits(self, length):
        ListOfBits = [random.randint(0, 1) for i in range(length)]
        self.bits = ListOfBits
alice = Communicator("Alice")
alice.genrateBits(8)
print(f"{alice.name}'s bits are: {alice.bits}")