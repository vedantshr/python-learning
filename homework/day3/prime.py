if __name__=="__main__":
    l = list(map(int, input().split(" ")))
    l1 = list()
    a = len(l)
    
    for i in range(a):
        b = l[0]
        for j in range(2,b):
            
            if b % j == 0:
                
                l1.append(1)
                break
        else:
            l1.append(0)
        l.remove(b)

    print(l1)