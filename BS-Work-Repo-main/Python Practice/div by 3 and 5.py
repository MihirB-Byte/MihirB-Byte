# This generates a qt4 python file
import sys, os.path, os, time, subprocess
x=1
ran_num=0

while (x==1):

 ran_num = int(input("Please enter a randon number"))
 if (ran_num%3==0 and ran_num%5==0):
     print("Number divisible by 3 and 5")
 elif (ran_num%3==0):
     print("Number divisible by 3")
 elif (ran_num%5==0):
     print("Number divisible by 5")
 x=input("press 1 to play again")

 
