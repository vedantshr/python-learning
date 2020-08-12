class Project:
    def __init__(self, projectId, projectName, manHours, technologyList, avgProjCost):
        self.projectId = projectId
        self.projectName = projectName
        self.manHours = manHours
        self.technologyList = technologyList
        self.avgProjCost = 0.0
    def calculateProjCost(self, ratePerManHour):
        if nameOfProject == self.projectId:
            return self.manHours*ratePerManHour


class Organisation:
    def __init__(self, orgName, Projlist):
        self.orgName = orgName
        self.Projlist = Projlist
    def projAvgCostByTechnology(self, ratePerManHour):
        avgProjCost = 0.0
        for objects in self.Projlist:
            if nameOfProject == objects.projectId:
                # projCost = objects.manHours*ratePerManHour
                objects.avgProjCost = (objects.calculateProjCost(ratePerManHour)/len(objects.technologyList))
                return objects.avgProjCost
                


if __name__ == "__main__":
    n = int(input())
    Projlist = []
    for i in range(n):    
        projectId = int(input())
        projectName = input()
        manHours = int(input())
        technologyList = list(map(str, input().split(" ")))
        obj = Project(projectId, projectName, manHours, technologyList, 0.0)
        Projlist.append(obj)
    nameOfProject = int(input())
    ratePerManHour = float(input())
    obj2 = Organisation("ABC", Projlist)
    # projcost = obj.calculateProjCost(ratePerManHour)
    averageCostOfProject = obj2.projAvgCostByTechnology(ratePerManHour)
    # print(projcost)
    print(averageCostOfProject)
    
        

