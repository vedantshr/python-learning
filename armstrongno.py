def armstrong(ip):
    n = 0
    for i in range(len(ip)):
        n = n + int(ip[i])**len(ip)

    if  n == int(ip):
        return True
    else:
        return False

if __name__ == "__main__":
    ip = input()
    ip2 = input()
    print (armstrong(ip))
    print (armstrong(ip2))