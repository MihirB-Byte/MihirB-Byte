import sys, os.path, os, time, subprocess, random


x=2

while(x==2):
    x =int (input("Press 1 to roll the dice"))
    if (x==1):
        print (random.randrange(1,6))
    else:
        exit
    x= int(input("Press 2 to play again"))




 