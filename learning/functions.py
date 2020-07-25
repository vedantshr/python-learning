import math

def firstFunction(name):
    letters = len(name)
    firstLetter = name[0]
    return (letters, firstLetter)

def decimalPlaces(num, dec):
    return round(num, dec)

if __name__ == "__main__":
    # inp = input()
    # integ, strin= firstFunction(inp)
    print (decimalPlaces(21.23456, 3))
    # print (integ, "\t", strin)
    print (math.ceil(1.00001))
    print ("gdjhgdhj*jgdhjgd bjhdmbduy gjgdjgdjy".split("*"))
    # l = [1,2,3]
    # print (list(map(float, l)))
    slt = list(map(int, input().split(" ")))
    print (slt)