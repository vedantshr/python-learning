class EMployee:
    def __init__(self, empId, empName, empDomain, empWorkHours, empSalary):
        self.empId = empId 
        self.empName = empName
        self.empDomain = empDomain
        self.empworkHours = empWorkHours
        self.empSalary = empSalary

class Salary:
    def __init__(self, companyName, empList):
        self.companyName = TCS
        self.empList = empList
        
if __name__ == "__main__":
    NumberOfEmployees = int(input())
    empList = []
    for i in range(NumberOfEmployees):
        empId = int(input())
        empName = str(input())
        empDomain = str(input(""))
        empWorkHours = float(input())
        if empDomain == "IT":
            empSalary = 20000 + (empWorkHours*500)
        elif empDomain == "HR":
            empSalary = 14000 + (empWorkHours*500)
        else:
            print("None")
        obj = EMployee(empId, empName, empDomain, empWorkHours, empSalary)
        empList.append(obj)
        print("\n",[obj.empName,obj.empSalary])
        print({empName:empId})
        empList.remove(obj)

