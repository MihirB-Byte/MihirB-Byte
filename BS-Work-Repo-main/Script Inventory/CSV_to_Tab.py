#!python2.6
import os, csv, sys

filelist = open(sys.argv[1], "r").read().split("\n")

for filename in filelist:
    if filename.split(".")[-1].lower() == "csv":
        outfname = ""
        for i in filename.split(".")[:-1]:
            outfname += i + "."
        outfname += "txt"
        f = open(filename, "rb")
        csvf = csv.reader(f)
        outf = open(outfname, "wb")
        outcsv = csv.writer(outf, delimiter = "\t")
        for i in csvf:
            outcsv.writerow(i)
        outf.close()
        f.close()

print "done"
