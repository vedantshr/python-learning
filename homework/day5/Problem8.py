import math

class Professor:
    def __init__(self, profId, profName, subjectsDict):
        self.profId = profId
        self.profName = profName
        self.subjectsDict = subjectsDict

class University:
    def __init__(self, listOfObj):
        self.listOfObj = listOfObj

    def getTotalExperience(self, inpProfId):
        for objects in self.listOfObj:
            if inpProfId == objects.profId:
                return objects.subjectsDict

    def selectSeniorProfessorBySubject(self, subjectName):        
        for objects in self.listOfObj:
            maxm = 0
            dictn = {}
            if subjectName == objects.subjectsDict:
                for i in objects.subjectsDict:
                    if maxm < i[subject]:
                        maxm = i[subject]
                        dictn = i
                    
            return (dictn,objects.profName)



if __name__ == "__main__":
    n = int(input())
    listOfObj = []
    for i in range(n):
        profId = int(input())
        profName = input()
        subjectsDict = {}
        n1 = int(input())
        for j in range(n1):
            subject = input()
            experience = int(input())
            subjectsDict[subject] = experience
            
            obj = Professor(profId, profName, subjectsDict)
        listOfObj.append(obj)
    inpProfId = int(input())
    subjectName = input()
    obj2 = University(listOfObj)
    exp = obj2.getTotalExperience(inpProfId)
    maxmExperience = obj2.selectSeniorProfessorBySubject(subjectName)
    print(exp)
    print(maxmExperience)





