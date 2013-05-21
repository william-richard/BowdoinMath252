import sys
import math

def getInt(msg):
    try:
        data = int(raw_input(msg + " "))
    except ValueError:
        data = int(raw_input("Invalid input.  Try again: "))
    return data

def main():
    #get our values
    first = getInt("Input the 1st number you would like to get the GCD for: ")
    second = getInt("Input the 2nd number you would like to get the GCD for: ")
    #make sure we get a > b
    if first > second:
        a = first
        b = second
    else:
        a = second
        b = first
    #set up r
    r = a%b
    while(r != 0):
        print 'r = ' + repr(r) + ' a = ' + repr(a) + ' b = ' + repr(b)
        a = b
        b = r
        r = a%b
    print 'DONE: r = ' + repr(r) + ' a = ' + repr(a) + ' b = ' + repr(b)
    print 'GCD = ' + repr(b)



if __name__ == "__main__":
    main()
