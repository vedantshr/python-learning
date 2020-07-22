if __name__ == "__main__":
    ip = input()
    n = 0
    for i in range(len(ip)):
        n = n + int(ip[i])**len(ip)

    if  n == int(ip):
        print("True")
    else:
        print("False")