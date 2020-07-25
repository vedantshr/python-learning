# def split(ip()):
#     return list(ip())

if __name__=="__main__":
    
    ip = list(input().split(" "))
    l = []
    l.append(ip[0])
    for i in range(1, len(ip)):
        if ip[i] not in l:
            l.append(ip[i])

    print(l)
