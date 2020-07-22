if __name__ == "__main__":
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
            
