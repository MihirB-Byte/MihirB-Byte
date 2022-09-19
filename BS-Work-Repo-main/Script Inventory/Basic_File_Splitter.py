#!python2.6
import csv, os, sys, os.path

path, filename = os.path.split(sys.argv[1])

#filename = raw_input("what is the name of the file? \n")
if len(sys.argv) > 2:
    headers = sys.argv[2] == "y"
else:
    headers = (raw_input("do these files contain headers? y/n \n").lower() == "y")

outfiles = {}
f = open(filename, "rb")

csvf = csv.reader(f)
if headers:
    header = csvf.next()[1:]

maxrowlen = 0

for row in csvf:
    if len(row) > 0:
        if row[0] not in outfiles:
            if headers:
                outfiles[row[0]] = [header]
            else:
                outfiles[row[0]] = []
        outfiles[row[0]].append(row[1:])
        maxrowlen = max(len(row),maxrowlen)

for file, rows in outfiles.items():
    out = open(file, "wb")
    outcsv = csv.writer(out)
    for i in rows:
        newrow = i[:]
        while len(newrow) < maxrowlen:
            newrow.append("")
        outcsv.writerow(i)
    out.close()