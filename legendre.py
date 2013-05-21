import sys
import math
import sys
import fermat

#do the first steps of the legendre symbol i.e. make sure bottom is actually prime
def legendre(top, bottom, print_info):
    #make sure bottom is actually prime
    bottomFactors = fermat.factor(bottom, 0)
    if(bottomFactors is None):
        #the bottom is actually prime
        answer = recurse(top, bottom, print_info)
        if(print_info):
            print "************\nOverall answer of (" + repr(top) + " on " + repr(bottom) + ") = " + repr(answer)
        return answer
    else:
        if(print_info):
            print "Bottom is not a prime"
        return None


#do all the recursion necessary to solve the Legendre Symbol of (top / bottom)
#we should already know that bottom is prime when we call this
def recurse(top, bottom, print_info):
    sys.stdout.flush()
    #first, if top > bottom, find the mod of top in terms of bottom so we have an easier problem
    if(print_info):
        print "Calculating (" + repr(top) + " on " + repr(bottom) + ")"

    if(top >= bottom):
        top = top % bottom
        #see if top = -1 (mod bottom), and assign that accordingly
        if(top == bottom-1):
            top = -1
        if(print_info):
            print "Which is equivalent to (" + repr(top) + " on " + repr(bottom) + ")"

    #see if top == 1, because we know that if that is the case this legendre = 1
    if(top == 1):
        if(print_info):
            print "Top == 1 - return 1\n"
        return 1

    #see if the top == -1 - we know how to solve that legendre easily
    if(top == -1):
        answer = math.pow(-1, (bottom-1)/2)
        if(print_info):
            print "Top == -1 - return " + repr(answer) + "\n"
        return answer

    #if top < 0, we know we can factor it into (-1)(-top), so do that
    if(top < 0):
        if(print_info):
            print "Top < 0 - calculate (-1 on " + repr(bottom) + ") * (" + repr(-1*top) + " on " + repr(bottom) + ")"
        answer = recurse(-1, bottom, print_info) * recurse(-1 * top, bottom, print_info)
        if(print_info):
            print "(-1 on " + repr(bottom) + ") * (" + repr(-1*top) + " on " + repr(bottom) + ") = " + repr(answer) + "\n"
        return answer


    #see if the top == 2 - we also know how to solve that legendre easily
    if(top == 2):
        bottomSquared = bottom * bottom
        answer = math.pow(-1, (bottomSquared - 1) / 8)
        if(print_info):
            print "Top == 2 - return " + repr(answer) + "\n"
        return answer

    #see if the top is a perfect square - if it is, we know this legendre == 1
    topSqrt = math.sqrt(top)
    if(topSqrt == math.floor(topSqrt)):
        #it is a perfect square - return 1
        if(print_info):
            print "Top is a perfect square - return 1\n"
        return 1
    #not a perfect square otherwise

    #see if the top can be factored
    #if it can be, take the legendre of the factors with the bottom
    #and multiply them together
    topFactors = fermat.factor(top, 0)
    if(topFactors is None):
        if(print_info):
            print "Top is prime: caculate (" + repr(top) + " on " + repr(bottom) + ") * (" + repr(bottom) + " on " + repr(top) + ")\n"
        #top is a prime
        #use quadratic reprocity
        #first, calculate it flipped upside down
        flippedLegendre = recurse(bottom, top, print_info)
        #next, calculate the product of the flipped an normal one using the formula
        exponent = ((top-1)/2)*((bottom-1)/2)
        product = math.pow(-1, exponent)
        #divide the product by the flipped one to get the answer of the one we want
        answer = product / flippedLegendre
        if(print_info):
            print "Top is prime - return " + repr(product) + "/" + repr(flippedLegendre) + "=" + repr(answer) + "\n"
        return answer
    else:
        #the top is not prime - do the legendre of both of the factors with the bottom
        #return their product
        if(print_info):
            print "Top is not prime - recurse on (" + repr(topFactors[0]) + " on " + repr(bottom) + ") * (" + repr(topFactors[1]) + " on " + repr(bottom) + ")\n"
        answer = recurse(topFactors[0], bottom, print_info) * recurse(topFactors[1], bottom, print_info)
        if(print_info):
            print "(" + repr(topFactors[0]) + " on " + repr(bottom) + ") * (" + repr(topFactors[1]) + " on " + repr(bottom) + ") = " + repr(answer) + "\n"
        return answer


def getLong(msg):
    try:
        data = long(raw_input(msg + " "))
    except ValueError:
        data = long(raw_input("Invalid input.  Try again: "))
    return data
    
def main():
    #get our value
    top = getLong("Input the top value of the legendre: ")
    bottom = getLong("Input the bottom value of the legendre: ")
    legendre(top, bottom, 1)

if __name__ == "__main__":
    main()
