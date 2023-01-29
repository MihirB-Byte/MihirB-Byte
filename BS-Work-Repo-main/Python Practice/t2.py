import random,sys

print(" Let play Rock Paper Scissors")

wins=0
loss=0
tie=0
randomRPSgen=0
Ch='y'

def rpsgen():
    randomstring_RPS= ["R","P","S"]
    random.shuffle(randomstring_RPS)
    return randomstring_RPS[0]
