import sys
import math
import fractions

def getInt(msg):
    try:
        data = int(raw_input(msg + " "))
    except ValueError:
        data = int(raw_input("Invalid input.  Try again: "))
    return data

def pollard(n):
    print "Trying to factor " + repr(n)
    #make sure factor is not even
    if((n % 2) == 0):
        print "Value is even! Factor = 2"
        return None
    #find prime divisors less than c
    stopValue = 100;
    c = 10000
    bigFactorial = math.factorial(c)
    print "going to stop when we try " + repr(stopValue)
    #start with 2, and calculate m 
    print "trying ",
    for x in range(2, stopValue):
        if(x == 2):
            print repr(x),
        else:
            print ", " + repr(x),
        sys.stdout.flush()
        m = pow(x, bigFactorial, n)
        if(m > 1):
            gcd = fractions.gcd(m-1, n)
            factors = [gcd, n/gcd]
            print "\n"
            print "the gcd of " + repr(n) + " and " + repr(m-1) + " is " + repr(gcd)
            print "factors of " + repr(n) + " are " + repr(factors[0]) + ", " + repr(factors[1])
            return factors
    print "\n"
    print "no factors found :-("
    return None



def main():
    #get our value
    n = getInt("Input the value that you want to determine a factor for, or if it is prime: ")
    #use pollard to find it's factors
    pollard(n)

if __name__ == "__main__":
    main()

