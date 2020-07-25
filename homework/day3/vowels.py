if __name__=="__main__":
    ip = input()

    v = ['a','e','i','o','u']
    for i in range(len(ip)):
        x = 0
        for j in range(len(ip)):
            if ip[j] in v:
                x = x + 1
    print(x)
