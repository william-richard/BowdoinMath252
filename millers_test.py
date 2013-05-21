import sys
import math

def test(n, b, print_info):
    #make sure n is odd
    if (n%2 is 0):
        if(print_info):
            print "n is even"
        #n is even, and thus composite
        return 1

    #make sure b is in the correct range
    if(b < 1 or b > n-1):
        if(print_info):
            print "b is not in correct range - b needs to follow 1 < b < n-1"
        #inconclusive test
        return 0

    #divide n-1 by 2 as many times as possible
    #this lets us find an odd co-factor s.t. n-1 = q * 2^k
    temp = n-1
    k = 0
    print repr(temp)
    while(temp % 2 == 0):
        k = k+1
        temp = temp /2
    q = (n-1) / math.pow(2, k)
    if(print_info):
        print "We have found an odd co-factor of n-1 = " + repr(n-1)
        print repr(n-1) + " = 2^" + repr(k) + " * " + repr(q)
    #set starting values for i
    i = 0
    r = math.pow(b, q) % n
    if(print_info):
        print " i = " + repr(i) + ":\t\t" + repr(b) + "^(" + repr(q) + " * 2 ^ " + repr(i) + ") = " + repr(r) + " (mod " + repr(n) + ")"
    # make sure we haven't aleady hit r = 1
    if(r == 1):
        #the test in inconclusive
        return 0
    while(i < k):
        if(print_info and i != 0):
            print " i = " + repr(i) + ":\t\t" + repr(b) + "^(" + repr(q) + " * 2 ^ " + repr(i) + ") = " + repr(r) + " (mod " + repr(n) + ")"
        # make sure r != -1 (mod n)
        if(r == n-1):
            #the test in inconclusive
            return 0
        #go to the next i and n
        i = i + 1;
        r = math.pow(b, q*2*i) % n
    #i is greater than k, and we have not gotten an inconclusive teste
    #thus we have a conclusive test
    return 1


def getLong(msg):
    try:
        data = long(raw_input(msg + " "))
    except ValueError:
        data = long(raw_input("Invalid input.  Try again: "))
    return data
    
def main():
    #get our value
    n = getLong("Input n, the value you test: ")
    base = getLong("Input b, the base to test: ")
    if(test(n, base, 1)):
        print repr(n) + " is composite"
    else:
        print "test on " + repr(n) + " is inconclusive"

if __name__ == "__main__":
    main()
