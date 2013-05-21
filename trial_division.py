import sys
import math

def getInt(msg):
    try:
        data = int(raw_input(msg + " "))
    except ValueError:
        data = int(raw_input("Invalid input.  Try again: "))
    return data

def test(n, print_info):
    #set up f
    f = 2.0
    #get the value of floorRootN, so we don't have to do it all the time
    floorRootN = math.floor(math.sqrt(n))
    if(print_info):
        print 'Floor sqrt(n) = ' + repr(floorRootN)
    #check to see if n/f is an integer
    while(math.floor(n/f) != n/f):
        #n/f is not an int, so keep going
        if(print_info):
            print 'Trying ' + repr(f)
        if(f > floorRootN):
            if(print_info):
                print 'PRIME!!!!'
            return None
        f+=1
    else:
        #n/f is an int, so we have a factor
        if(print_info):
            print 'Factor = ' + repr(f)
        return [f, n/f]




def main():
    #get our value
    n = getInt("Input the value that you want to determine the smallest factor for, or if it is prime: ")
    test(n, 1)
    

if __name__ == "__main__":
    main()

