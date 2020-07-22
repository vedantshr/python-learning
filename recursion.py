def factorial(no):
    # print (no)
    if no == 1:
        return 1
    else:
        return factorial(no-1)*no

if __name__ == "__main__":
    no = int(input())
    print("function call ended\t", factorial(no))