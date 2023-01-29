#!python3.6
import os, os.path, sys
import win32com.client

constants = win32com.client.constants
f = open(sys.argv[1], "r")
files = f.read().split("\n")
f.close()
try:
    excel = win32com.client.DispatchEx('Excel.Application')
except:
    import win32com
    import shutil
    genCache = win32com.__gen_path__
    for folder in os.listdir(genCache):
        if os.path.isdir(os.path.join(genCache,folder)):
            shutil.rmtree(os.path.join(genCache, folder))
    input("There was an error with the cache, it has now been cleared. Please re-run to convert")
    sys.exit()
excel.Visible = False

cwd = os.getcwd()

excel.Application.DisplayAlerts = False

try:

    for xls in files:
        filename, ext = os.path.splitext(xls)
        fullPath = os.path.join(cwd, filename)
        if ext.lower() not in (".xls",".xlsx",".xlsm", ".xml"):
            continue
        doc = excel.Workbooks.Open(os.path.join(os.getcwd(),xls))
        x = 0

        sheetList = []
        for i in doc.Worksheets:
            foundSheets = True
            if i.UsedRange() != None and i.Visible:
                sheetList.append(i.Name)
        else:
            for i in doc.Worksheets:
                if i.Name in sheetList:
                    if len(sheetList) == 1:
                        name = "%s.csv" % (fullPath)
                    else:
                        newname  = i.Name
                        for x in "/\\;:*?":
                            newname = newname.replace(x,"")
                        name = "%s_%s.csv" % (fullPath, newname)

                    i.Activate()
                    doc.SaveAs(name, 62)
                del i
        x = sheetList.pop()
        del x
            
        excel.ActiveWorkbook.Close(False)
        del doc
    
    
    if excel.ActiveWorkbook == None:
        excel.Application.Quit()
    else:
        excel.Visible = True
        excel.Application.DisplayAlerts = True
    del excel
except:
    excel.Visible = True
    excel.Application.DisplayAlerts = True


    
    
