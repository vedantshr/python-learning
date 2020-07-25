import os, csv
if __name__ == "__main__":
    try:
        #code to executed
        i = 12
        while (i>0):
            print ("infinite loop")

        with open("csvfile/a.csv", "r") as f:
            readobj = csv.reader(f)
            for row in readobj:
                print (row)
        f.close()
    except os.error:
        #code to be executed if error pops ip
        print ("vhjhgjhghj doesnot exist")
    except ZeroDivisionError:
        print ("file doesnot exist")
    except KeyboardInterrupt:
        print ("keyboard interrupt")