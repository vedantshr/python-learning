if __name__ == "__main__":
    n = int(input())
    output = 1

    for i in range(2,n+1):
        output = output * i

    print (output)