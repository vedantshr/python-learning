import csv
def writeCSV(n):
    f = open("csvfile/problem.csv", "w")
    writeobj = csv.writer(f)
    writeobj.writerow(["Name","Age","Gender"])

    for i in range(n):
        l = input().split(" ")
        writeobj.writerow(l)
    f.close()

def printCSV():
    f = open("csvfile/problem.csv","r")
    readobj = csv.reader(f)
    for i in readobj:
        print(i)
    f.close()

if __name__ == "__main__":
    n = int(input())
    writeCSV(n)
    printCSV()
