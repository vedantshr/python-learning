if __name__ == "__main__":
    
#Fibonacci Sequence
    ip = int(input())
    x = 0
    y = 1
   
    print(x,"\n",y)
    for s in range(2,ip):
        s = x + y 
        print("\n",s)
        x = y
        y = s
            
   
