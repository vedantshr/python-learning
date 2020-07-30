if __name__ == "__main__":
    n = int(input())
    l = []
    for n in range(n):
        name = input()
        score = float(input())
        l.append([name, score])

    l = sorted(l)

    print (l)

    # n = int(input())
    # l = list()
    # l1 = list()
    # for n in range(n):
    #     name = input()
    #     score = float(input())
    #     l.append(name)
    #     l1.append(score)
    # print(l,"\n",l1)
    
    # for i in range(len(l1)):
    #     mini = l1[0]
    #     for j in range(len(l1)):
    #         if mini > l1[j]:
    #             mini = l1[j]
    #         x = l1.index(mini)
    # l.remove(l[x])
    # l1.remove(mini)
    # print(l,"\n",l1)
    
    # for i in range(len(l1)):
    #     minm = l1[0]
    #     for j in range(len(l1)):
    #         if minm > l1[j]:
    #             minm = l1[j]
    #         x = l1.index(minm)
    # print(l[x])



               
