import sys
import math

def getInt(msg):
    try:
        data = int(raw_input(msg + " "))
    except ValueError:
        data = int(raw_input("Invalid input.  Try again: "))
    return data

def factor(n, print_info):
    #make sure it is not even
    if((n % 2) == 0):
        if(print_info):
            print "Value is even! Factor = 2"
        return [2, n/2]
    #set up x
    x = math.floor(math.sqrt(n))
    if(print_info):
        print "starting with x = " + repr(x)
    #make sure we don't have a factor
    if(x*x == n):
        if(print_info):
            print "Factor = " + repr(x)
        return [x,x]
    #keep going - start by incrementing x
    x += 1
    if(print_info):
        print "going to stop when x = " + repr( ((n+1)/2) )
    while(x < (n+1)/2):
        y = math.sqrt(x*x - n)
        if(print_info):
            print "x = " + repr(x) + ", y = " + repr(y) + "\t",
        #see if y is an integer
        if(math.floor(y) == y):
            if(print_info):
                print "\n"
                print "not prime"
                print "factors of " + repr(n) + " are " + repr(x + y) + " and " + repr(x - y)
            return [x+y, x-y]
        x += 1
    else:
        #x >= (n+1/2), so n is prime
        if(print_info):
            print "\n"
            print repr(n) + " is PRIME!"
        return None



def main():
    #get our value
    n = getInt("Input the value that you want to determine a factor for, or if it is prime: ")
    factor(n, 1)
    




if __name__ == "__main__":
    main()

