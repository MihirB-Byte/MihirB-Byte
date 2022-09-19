#!python2.6
import csv, sys, os, os.path
files = open(sys.argv[1]).read().split("\n")
for filename in files:
    f = open(filename, "rb")
    csvf = csv.reader(f)
    oname = os.path.splitext(filename)[0] + "_CRLF_replaced" + os.path.splitext(filename)[1]
    o = open(oname, "wb")
    csvo = csv.writer(o)
    for row in csvf:
        for i in range(len(row)):
            row[i] = row[i].replace(chr(13)+chr(10), "|")
            row[i] = row[i].replace(chr(13), "|").replace(chr(10), "|")
        csvo.writerow(row)
    o.flush()
    o.close()
