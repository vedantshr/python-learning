def dictMax(lstofDict):
    maxi = 0
    dictionaryOp = {}
    for dictionary in lstofDict:
        for key in dictionary:
            if maxi < dictionary[key]:
                maxi = dictionary[key]
                dictionaryOp = dictionary
    return dictionaryOp

if __name__ == "__main__":
    n = int(input())
    lstofDict = []
    while n>0:
        key = input()
        val = int(input())
        lstofDict.append({key:val})
        n = n-1

    print (dictMax(lstofDict))