class Employee:
    def __init__(self, empId, empName, empDomain, empWorkHours, empSalary):
        self.empId = empId 
        self.empName = empName
        self.empDomain = empDomain
        self.empWorkHours = empWorkHours
        self.empSalary = empSalary

class Salary:
    def __init__(self, companyName, empList):
        self.companyName = companyName
        self.empList = empList

    def setSalary(self, empSalId):
        for objects in self.empList:
            if empSalId == objects.empId:
                if objects.empDomain == "IT":
                    objects.empSalary = 20000 + (objects.empWorkHours*500)
                elif objects.empDomain == "HR":
                    objects.empSalary = 14000 + (objects.empWorkHours*500)
                return objects
        return "D.E."

    def deletEmployee(self, delEmpId):
        dict1 = {}
        for objects in self.empList:
            if delEmpId == objects.empId: 
                dict1[objects.empId] = objects.empName
                empList.remove(objects)
                return dict1
        return "D.E."

if __name__ == "__main__":
    noOfEmployees = int(input())
    empList = []
    for i in range(noOfEmployees):
        empId = int(input())
        empName = input()
        empDomain = input()
        empWorkHours = int(input())
        obj = Employee(empId, empName, empDomain, empWorkHours, 0.0)
        empList.append(obj)
    
    empSalId = int(input())
    delEmpId = int(input())
    obj2 = Salary("TCS", empList)
    SetSalary = obj2.setSalary(empSalId)
    DeletedEmployee = obj2.deletEmployee(delEmpId)
    if type(SetSalary) is str:
        print(SetSalary)
    else:
        print(SetSalary.empId, SetSalary.empName, SetSalary.empDomain, SetSalary.empWorkHours, SetSalary.empSalary)
    print(DeletedEmployee)

