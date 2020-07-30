if __name__ == "__main__":
    try:
        a = int(input())
        b = int(input())
        print(a/b)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")
        
