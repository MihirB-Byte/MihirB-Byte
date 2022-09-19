#!python2.6
import csv
import xlwt
import sys
import os
import os.path

files = open(sys.argv[1], "rb").read().split("\n")
xlfile = xlwt.Workbook()
textStyle = xlwt.easyxf(num_format_str="@")

for filename in files:
    if os.path.splitext(filename)[1].lower() <> ".csv":
        continue
    outfilename = os.path.splitext(filename)[0] + "_.xls"
    xlfile = xlwt.Workbook()
    sheetname = os.path.splitext(os.path.split(filename)[1])[0][:31]
    xlsheet = xlfile.add_sheet(sheetname)

    
    f = open(filename, "rb")
    csvf = csv.reader(f)
    rowNo = 0
    for row in csvf:
        colNo = 0
        for cell in row:
            xlsheet.write(rowNo, colNo, str(cell), textStyle)
            colNo += 1
        rowNo += 1
    f.close()
    xlfile.save(outfilename)
        
        
