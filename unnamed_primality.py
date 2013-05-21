import sys
import math
import trial_division
from pow_mod import modOfPower

def test(n, print_info):
    #set up a dictonary to store the prime factors and their exponent
    #the key is the factor, the values are the exponents
    factorization = {}

    temp = n-1
    #factor temp until it is prime
    f = trial_division.test(temp, 0)
    while(f is not None):
        temp = f[1]
        if f[0] in factorization:
            factorization[f[0]] = factorization[f[0]]+1
        else:
            factorization[f[0]] = 1
        f = trial_division.test(temp, 0)
    #now, temp is the last prime factor
    if temp in factorization:
        factorization[temp] = factorization[temp]+1
    else:
        factorization[temp] = 1

    if(print_info):
        print "n-1 = " + repr(n-1) + " = " + repr(factorization)

    #try to find a b that matches the criteria for each prime factor of n-1
    for p in factorization.keys():
        foundB = False
        #go from 2 to n-1, so ask for range between 2 and n (range does not inclued n)
        for b in xrange(2, n):
            if(modOfPower(b, n-1, n) == 1 and modOfPower(b, int((n-1)/p), n) != 1):
                #we found a b matching our criteria
                if print_info:
                    print ""
                    print repr(b) + "^" + repr(n-1) + " = 1 (mod " + repr(n) + ")"
                    print "and " + repr(b) + "^" + repr(n-1) + "/" + repr(p) + " != 1 (mod " + repr(n) + ")"
                    print ""
                foundB = True
                break
        #if we did not find b, then n is not prime
        if not foundB:
            if print_info:
                print "\n no b found for " + repr(p) + " so " + repr(n) + " is NOT prime\n"
            return False
    #if we got here, we found all the b's we needed
    if print_info:
        print repr(n) + " is PRIME!!!"
    return True


def getLong(msg):
    try:
        data = long(raw_input(msg + " "))
    except ValueError:
        data = long(raw_input("Invalid input.  Try again: "))
    return data


def main():
    #get our value
    n = getLong("Input n, the value to test the primality of: ")
    test(n, 1)

if __name__ == "__main__":
    main()
