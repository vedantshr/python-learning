class Student:
    def __init__(self, nameSt, sub1, sub2, sub3):
        self.nameSt = nameSt
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def calculateResult(self, nameOfStudent):
        for objects in studentDict:
            if nameOfStudent == objects.nameSt:
                if objects.sub1 > 40 and objects.sub2 > 40 and objects.sub3 > 40:
                    return (objects.sub1 + objects.sub2 + objects.sub3)/3
                else:
                    return 0

class School:
    def __init__(self, name, studentDict):
        self.name = name
        self.studentDict = studentDict

    def getStudentResult(self):
        for objects in self.studentDict:
            if avg > 60:
                value = "Pass"
                return value
            else:
                value = "Fail"
                return value

    def findStudentWithHighestMarks(self):
        l = []
        for objects in self.studentDict:
            if (objects.sub1 + objects.sub2 + objects.sub3)/3 > 60:
                l.append((objects.sub1 + objects.sub2 + objects.sub3)/3)
        return [max(l)]




if __name__ == "__main__":
    n = int(input())
    studentDict = {}
    value = ""
    l = []
    for i in range(n):
        nameSt = input()
        sub1 = float(input())
        sub2 = float(input())
        sub3 = float(input())
        obj = Student(nameSt, sub1, sub2, sub3)
        studentDict[obj] = value

    nameOfStudent = input()
    obj2 = School("SMAPS", studentDict)
    avg = obj.calculateResult(nameOfStudent)
    result = obj2.getStudentResult()
    highestmarks = obj2.findStudentWithHighestMarks()
    print(avg)
    print(result)
    print(highestmarks)






