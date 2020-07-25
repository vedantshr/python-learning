import os, csv

f = open("csvfile/test.csv", "w")
writeobj = csv.writer(f)
writeobj.writerow(["Alphabet", "Number"])
x = 65
for i in range(1,27):
    writeobj.writerow([chr(x), i])
    x=x+1
f.close()

with open("csvfile/test.csv", "r") as f:
    readobj = csv.reader(f)
    for row in readobj:
        print (row)
f.close()