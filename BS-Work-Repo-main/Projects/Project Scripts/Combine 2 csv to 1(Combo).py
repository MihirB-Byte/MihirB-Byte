import csv
import array
import os
import sys

files = []


Headers = []
Data = []
outf = open("Test2.csv", "w")
Datafile2 = csv.writer(outf)
"""
with open('Test3.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name','Company','Address1','Address2']
    csv_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_write.writeheader()
    csv_write.writerow({'Name' : 'Mihir','Company': 'Bluestar' ,'Address1': 'Lower hutt','Address2':'WLG'})
    csv_write.writerow({'Name' : 'Mihir1','Company': 'Bluestar1' ,'Address1': 'Lower hutt1','Address2':'WLG1'})"""

#for file in files:
with open('Test1.csv','r') as f:
    Datafile1 = csv.reader(f)
    print("Open Test1.csv file")
    with open('Test2.csv', 'w') as csv2_file:
        print("Open Test2.csv file")
        for row in Datafile1:
            Datafile2.writerow(row)
            



"""
    with open('Test2.csv', 'w') as csv2_file:
        
        print("Open Test2.csv file")
        
        with open('Test1.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            print("Open Test1.csv file")        
            Data = csv_reader   
            for row in Data:
                Data2=fileWriter.writerow(row)
                print("Writing in t2")

"""