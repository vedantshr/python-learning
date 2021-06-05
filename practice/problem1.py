import math
if __name__ == "__main__":
    heightOfCutter = int(input())
    noOfSticks = int(input())
    l = list(map(int, input().split(" ")))
    x = 0
    for i in range(noOfSticks):
        if l[x] > heightOfCutter:
            l[x] = heightOfCutter
        x = x + 1
    print(x)