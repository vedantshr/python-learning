class Student:
    def __init__(self, nameSt, sub1, sub2, sub3):
        self.nameSt = nameSt
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def calculateResult(self):
        if self.sub1 > 40 and self.sub2 > 40 and self.sub3 > 40:
            return (self.sub1 + self.sub2 + self.sub3)/3
        else:
            return 0

class School:
    def __init__(self, name, studentDict):
        self.name = name
        self.studentDict = studentDict

    def getStudentResult(self):
        for objects in self.studentDict:
            if objects.calculateResult() > 60:
                self.studentDict[objects] = "Pass"
            else:
                self.studentDict[objects] = "Fail"
        return self.studentDict

    def findStudentWithHighestMarks(self, passed_students):
        highest = 0
        student_name = "No student Passed."
        for obj in passed_students:
            if highest < obj.calculateResult():
                highest = obj.calculateResult()
                student_name = obj.nameSt
        return student_name, highest


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

    obj2 = School("SMAPS", studentDict)
    result = obj2.getStudentResult()
    passed_students = []
    for objects in result:
        if result[objects] == "Pass":
            passed_students.append(objects)
    stu, highestmarks = obj2.findStudentWithHighestMarks(passed_students)
    # print(avg)
    print(result)
    print(stu, highestmarks)






