import sys
import math

# def calc(b, p, mod, print_info):
#     #b is the base
#     #n is the power
#     #mod is the mod
#     #first, using fermat's thm, find what p is congruent to mod <mod-1>
#     small_p = p % (mod-1)
#     #now calculate b^small_p mod <mod>
#     answer = math.pow(b, small_p) % mod
#     if(print_info):
#         print repr(b) + " ^ " + repr(p) + " = " + repr(b) + " ^ " + repr(small_p) + " = " + repr(answer) + " mod " + repr(mod)

def modOfPower(base, power, mod):
    base1 = base % mod
    p = 1
    while power > 0:
        if((power % 2) == 1):
            p = base1 * p
            p = p % mod
        power = power/2
        base1 = (base1 * base1) % mod
    return p
    #instead of doing brute force, do exponential by squaring
    # for i in range(1, power+1):
    #     p = p*base1
    #     p = p % mod
    # return p

def getLong(msg):
    try:
        data = long(raw_input(msg + " "))
    except ValueError:
        data = long(raw_input("Invalid input.  Try again: "))
    return data
    
def main():
    #get our value
    b = getLong("Input the base of the power: ")
    p = getLong("Input the power of the base: ")
    mod = getLong("Input the mod you want to find: ")
    print modOfPower(b, p, mod)

if __name__ == "__main__":
    main()

