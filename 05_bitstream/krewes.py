'''
Team: Joseph Jeon, Joshua Liu

DISCO:

QCC:
'''

import random

Test = "8$$$Joshua Liu$$$Ducky@@@3$$$RandomPerson$$$Duckling@@@100$$$MickeyMouse$$$Cat"
def choose():
    Profiles = Test.split("@@@")
    randomPerson = random.choice(Profiles)
    Data = randomPerson.split("$$$")
    return Data[1] + " from period" + Data[0] + " has a ducky named: " + Data[2]

        
print(choose())