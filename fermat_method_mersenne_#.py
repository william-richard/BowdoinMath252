import sys
import math
import fermat

def fermatsMethod(p, print_info):
    #make sure p is prime and greater than 2
    if( (p <=2) or (fermat.factor(p, 0) is not None)):
        if(print_info):
            print repr(p) + " is not prime and greater than 2"
        return None

    #calculate M(p)
    # m = math.pow(2, p) - 1

    #calculate the upper limit of our search
    upperLimit = int((math.pow(2, p/2) - 1) / (2*p))

    if(print_info):
        print "M(" + repr(p) + ") = " + repr(m)
        print "going to test values of r until we reach " + repr(upperLimit)

    #start testing for an even division
    #i.e. see if q | M(p) or if M(p) = 0 (mod q)
    for r in range(1, upperLimit+1):
        q = 1+2*r*p
        if(print_info):
            print "r = " + repr(r) + "\t q = 1 + 2*" + repr(r) + "*" + repr(p) + " = 1 + " + repr(2*r*p) + " = " + repr(q)
        if(m % q == 0):
            if(print_info):
                print repr(q) + " is a divisor of M(" + repr(p) + ")"
            return q
        else:
            if(print_info):
                print repr(q) + " is NOT a divisor of M(" + repr(p) + ")"
    if(print_info):
        print "M(" + repr(p) + ") is prime"
    return None




def getLong(msg):
    try:
        data = long(raw_input(msg + " "))
    except ValueError:
        data = long(raw_input("Invalid input.  Try again: "))
    return data
    
def main():
    #get our value
    p = getLong("Input p, the value for M(p) that you want to factor: ")
    fermatsMethod(p, 1)

if __name__ == "__main__":
    main()
