if __name__ == "__main__":
    inp = int(input())
    for i in range(inp,0,-2):
        print(" "*((inp-i)//2), "*"*i, "\n")

#Fibonacci Sequence
    # ip = int(input())
    # x = 0
    # y = 1
   
    # print(x,"\n",y)
    # for s in range(2,ip):
    #     s = x + y 
    #     print("\n",s)
    #     x = y
    #     y = s
            
    print("Choose from the following figures : ", "\n","square \trectangle\ttriangle\tcircle")
    ip = str(input())
    print("What do you want to calculate ?","\n","Area \t Perimeter")
    ip2 = str(input())
    if ip2 == "area" :
        if ip == "square":
        elif ip == "rectangle":
        elif ip == "triangle":
        elif ip == "circle":
        else:
            print ("Invalid option")
    elif ip2 == "perimeter":
        if ip == "square":
        elif ip == "rectangle":
        elif ip == "triangle":
        elif ip == "circle":
        else:
            print ("Invalid option")
    else:
        print ("Invalid option")
            
