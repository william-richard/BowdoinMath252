import sys
import math
from pow_mod import modOfPower

def decrypt(n, d, eBlock):
    #decrypt the block
    dBlock = modOfPower(eBlock, d, n)
    print "clear block is " + repr(dBlock)
    #translate it to text, using the conversion from the book
    #where a = 10 and 99 = ' '
    clearText = ""
    for i in range(0, 200):
        nextLetter = int((dBlock / pow(10, i*2)) % 100)
        if nextLetter is 0:
            break
        if nextLetter is 99:
            clearText = ' ' + clearText
        #in python, 65 is 'A', so let's just add 55 to our values (where 'A' is 10) and use that
        else:
            clearText = chr(nextLetter + 55) + clearText
    return clearText


def getLong(msg):
    try:
        data = long(raw_input(msg + " "))
    except ValueError:
        data = long(raw_input("Invalid input.  Try again: "))
    return data
    
def main():
    #get n
    n = getLong("Please input n: ")
    #get d
    d = getLong("Please input d: ")

    #get our values and translate them
    eBlock = getLong("Please input the next block to decrypt, or -1 to exit")
    while eBlock != -1:
        print "'" + str(decrypt(n, d, eBlock)) + "'"
        eBlock = getLong("Please input the next block to decrypt, or -1 to exit")

    

if __name__ == "__main__":
    main()
