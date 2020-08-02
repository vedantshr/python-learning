class Bill:
    def __init__(self, mobileNumberB, paymentBill):
        self.mobileNumberB = mobileNumberB
        self.paymentBill = paymentBill

class Mobile:
    def __init__(self, serviceProvider, mobileNumberM, dataUsed, paymentMethod):
        self.serviceProvider =serviceProvider
        self.mobileNumberM = mobileNumberM
        self.dataUsed = dataUsed
        self.paymentMethod = paymentMethod

def calculateBills(listOfObj):
    listOfBill = []
    for mob in listOfObj:
        if mob.serviceProvider == "Airtel":
            paymentBill = (mob.dataUsed*11)
            if mob.paymentMethod == "Paytm":
                paymentBill = paymentBill - (paymentBill/10)
        elif mob.serviceProvider == "Jio":
            paymentBill = (mob.dataUsed*10)
        billObj = Bill(mob.mobileNumberM, paymentBill)
        listOfBill.append(billObj)
    return listOfBill

if __name__=='__main__':
    l=[]
    count=int(input())
    for i in range(count):
        sp=input()
        no=int(input())
        net=int(input())
        p=input()
        l.append(Mobile(sp,no,net,p))
    # demo=Mobile("",0,0,"")
    listOfBill=calculateBills(l)
    for i in listOfBill:
        print(i.mobileNumberB,i.paymentBill)
        


        


