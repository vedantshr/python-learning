class Pattern:
    def __init__(self, noOflines, character):
        self.noOflines = noOflines
        self.character = character
    
    def square(self):
        for i in range(self.noOflines):
            for j in range(self.noOflines):
                print (self.character,"\t", end="")
            print ("\n")

    def RightAngleTriangle(self):
        x = 1
        for i in range(self.noOflines):
            for j in range(x):
                print(self.character,"\t", end="")
            print("\n")
            x = x + 1

    def EquilateralTriangle(self):
        x = 1
        y = self.noOflines
        
        for i in range(self.noOflines):
            for j in range(y):
                print(end=" ") 
            for j in range(x):
                print(self.character,end=" ")
            print("\n")
            x = x + 1
            y = y - 1

    def Diamond(self):
        x = 1
        y = self.noOflines
        
        for i in range(self.noOflines):
            for j in range(y):
                print(end=" ") 
            for j in range(x):
                print(self.character,end=" ")
            print("\n")
            x = x + 1
            y = y - 1

        m = self.noOflines-1
        n = 1
        for i in range(self.noOflines-1):
            for j in range(n):
                print(end=" ")
            for j in range(m):
                print("",self.character,end="")
            print("\n")
            m = m - 1
            n = n + 1

    def Circle(self):
        x = 8
        y = int(self.noOflines*10)
        for i in range(int(self.noOflines*1.5)):
            # for j in range(y):
            print(" "*y, (self.character+" ")*x)
            # for j in range(x):
            print("\n")
            x = x + 10
            y = y - 7
        m = self.noOflines - 1
        n = 2
        for i in range(self.noOflines-2):
            for j in range(n):
                print(end=" ")
            for j in range(m+1):
                print("",self.character,end="")
            print("\n")
            m = m - 2
            n = n + 3