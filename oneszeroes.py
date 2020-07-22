if __name__ == "__main__":
    ip = list(map(int, input().split(" ")))
    n = 0 
    for i in range(len(ip)):
        if ip[i] == 1:
            n=n+1
    print ("Original= ", n)

    print ("Efficient= ", sum(ip))