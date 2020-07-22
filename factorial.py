def factorial(n):
    output = 1

    for i in range(2,n+1):
        output = output * i
    return (output)


if __name__ == "__main__":
    n = int(input())
    print(factorial(n))