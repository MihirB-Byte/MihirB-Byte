#!python2.6
import csv, os, sys, os.path
filenames = sys.argv[1].split("*")

headers = (raw_input("does this file contain headers? y/n\n").lower() == "y")

if headers:
    columnheader = raw_input("enter the name of the column to split on\n")
else:
    col = int(raw_input("enter the column number to split on\n")) - 1

counter = raw_input("would you like a counter appended to the filename? y/n \n").lower() =="y"

if headers:
    outputHeaders = raw_input("do you want to output headers? y/n \n").lower() == "y"
else:
    outputHeaders = False

for filename in filenames:

    fnoext = os.path.splitext(filename)[0]
    

    outfiles = {}
    f = open(filename, "rb")

    csvf = csv.reader(f)
    if headers:
        header = csvf.next()[:]
        col = header.index(columnheader)
    x = 1
    counternames = {}
    data = []
    for row in csvf:
        data.append(row)

    for row in data:
        splitText = row[col].replace("/","_").replace("\\","_")
        
        if splitText not in counternames:
            if counter:
                counternames[splitText] =  ("%0" + str(len(str(len(data)))) + "d")% x + " - " + splitText
                outfiles[counternames[splitText]] = []
                
                x+=1
            else:
                counternames[splitText] = splitText 
                outfiles[counternames[splitText]] = []

        outfiles[counternames[splitText]].append(row[:])

    for file, rows in outfiles.items():
        out = open(fnoext + " - " + file+".csv", "wb")
        outcsv = csv.writer(out)
        if outputHeaders:
            outcsv.writerow(header)
        for i in rows:
            outcsv.writerow(i)
        out.close()

