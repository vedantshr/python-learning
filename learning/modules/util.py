class Pattern:
    def __init__(self, noOflines, character):
        self.noOflines = noOflines
        self.character = character
    
    def square(self):
        for i in range(self.noOflines):
            for j in range(self.noOflines):
                print (self.character,"\t", end="")
            print ("\n")

class abc:
    def a(self):
        print (",nvkjdnvkjhsukh")