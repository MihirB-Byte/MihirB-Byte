#!python2.6
import csv
import os.path
import os
import sys
from collections import defaultdict

path, infilename = os.path.split(sys.argv[1])



#infilename = raw_input("enter the name of the file\n")
infile = csv.reader(open(infilename,"rb"))

outfilename = infilename[:-4] + "_reprints.csv"
if not os.path.exists(outfilename):
    f = open(outfilename, "w")
    f.close()
    del f
    
headers = raw_input("does this file contain headers? y/n\n")=="y"


if headers:
    headerCols = infile.next()
    column = headerCols.index(raw_input("enter the name of the identifier column\n"))
else:
    column = int(raw_input("what column number is the identifier?\n"))-1

prefix = raw_input("what is the prefix? leave blank if none\n")
suffix = raw_input("what is the suffix? leave blank if none\n")
outfile = csv.reader(open(outfilename,"rb"))

records = defaultdict(list)
outrecords = defaultdict(list)

for i in infile:
    records[i[column]].append(i)

for i in outfile:
    outrecords[i[column]].append(i)

outf = open(outfilename,"ab")
outfile = csv.writer(outf)
if headers:
    outfile.writerow(headerCols)
done = False

while not done:
    user_input = raw_input("enter next record or press enter to finish\n")
    record = prefix + user_input + suffix
    
    if record in records and record not in outrecords:
        for row in records[record]:
            outrecords[record].append(row)
            outfile.writerow(row)
        print records[record]
    elif user_input == "":
        done = True
        outf.close()
        print "done"
    
    elif record in outrecords:
        print "record already found"
    else:
        print "record not found"
        
