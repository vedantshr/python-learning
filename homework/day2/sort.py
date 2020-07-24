if __name__ == "__main__":
    l = list(map(int, input().split(" ")))
    l1 = list()
    
    x = len(l)
    for i in range(x):
        minm = l[0]
        for j in range(len(l)):
            if minm > l[j]:
                minm = l[j]
        l.remove(minm)
        l1.append(minm)
    print(l1)
     
    # l.sort()
    # print(l)
