if __name__ == "__main__":
    l = str(input())
    l1 = chr(input())
    x = 0
    for i in range(len(l)):
        if l1 in l:
            x = x + 1
    print(x)
