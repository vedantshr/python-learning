if __name__ == "__main__":
    n = int(input())
    l = list(input().split(" "))

    l.append('1')
    if n == 0:
        print(l)
    l.remove(l[0])
    if n == 1:
        print(l)
    l.insert(0,'1')
    if n == 2:
        print(l)
    l.sort()
    if n == 3:
        print(l)
    l.pop(1)
    if n == 4:
        print(l)
    l.reverse()
    if n >=5:
        print(l)       
        
            
            
    



    
    