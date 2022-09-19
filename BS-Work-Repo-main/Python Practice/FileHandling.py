import csv

#Open file in the same dir
f = open("FilehandlingTest.csv", "r")
type(f)
csvreader = csv.reader(f)
header = []
header = next(csvreader)

rows = []
for row in csvreader:
        rows.append(row)
print(header)
print(rows)

f.close()


#Open file in different location
"""f = open("P:\One off jobs\Eship Locals.csv", "r")
print(f.read())
f.close()"""

