#!python2.6
import csv, os, os.path
import sys


#files = sys.argv[1].split("*")
files = open(sys.argv[1], "r").read().split("\n")



headers = (raw_input("do these files contain headers?, y/n\n") == "y")
fileNo = 0
outf = open("combo.csv", "wb")
outcsv = csv.writer(outf)

for file in files:
    if os.path.splitext(file)[1].lower() in [".csv", ".bck", ".txt"] and os.path.split(file) != "combo.csv":

        maxrowlen = 0
        f = open(file, "rb")
        csvf = csv.reader(f)
        for row in csvf:
            maxrowlen = max(maxrowlen,len(row))
        f.close()
        del f
        del csvf
        maxrowlen += 1
        
                
        f = open(file, "rb")
        csvf = csv.reader(f)
        if fileNo == 0:
            fileNo += 1
            if headers:
                newrow = csvf.next()
                newrow.insert(0,"file")
                outcsv.writerow(newrow)
        else:
            if headers:
                csvf.next()
        for row in csvf:
            newrow = row
            newrow.insert(0, os.path.split(file)[1])
            while len(newrow) < maxrowlen:
                newrow.append("")
            outcsv.writerow(newrow)
            
        f.close()
        
outf.close()
