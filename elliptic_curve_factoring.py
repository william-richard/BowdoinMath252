from fractions import gcd

def extEuclideanAlg(a, b) :
  """Computes a solution  to a x + b y = gcd(a,b), as well as gcd(a,b)
  """
  if b == 0 :
      return 1,0,a
  else :
      x, y, gcd = extEuclideanAlg(b, a % b)
      return y, x - y * (a // b),gcd

def modInvEuclid(a,m) :
  """Computes the modular multiplicative inverse of a modulo m,
  using the extended Euclidean algorithm
  """
  x,y,gcd = extEuclideanAlg(a,m)
  if gcd == 1 :
      return x % m
  else :
      return None

#(px, py) is the orriginal point
#(x, y) is the current point that we have - i.e. some multiple of P
# A, B are from the elliptic curve E
#n is the value we want to factor
#print_info is a boolean to decide if we print information
def factor(px, py, A, B, n, print_info) :
  #first, start seeing if we can add P to P
  # Assert 2y (the y coordinate of the point) has a multiplicative inverse
  # If it does not, we have a factor of n
  inverse = modInvEuclid(2*py, n)
  if(print_info):
    print "Inverse of " + repr(2*py) + " is " + repr(inverse)
  if(inverse is None):
    #we have found a factor - return it
    f = gcd(2*py, n)
    if(print_info):
      print "FOUND A FACTOR: " + repr(f)
    return f
  #we don't have a factor - need to compute 2P, since (x,y) is original point
  lamda = ((3*(px*px) + A) * inverse) % n
  x = (lamda*lamda - px - px) % n
  y = (lamda * (px - x) - py) % n
  if(print_info):
    print "no factor found - making next point"
    print "for 2P: lamda = " + repr(lamda) + " new x = " + repr(x) + " new y = " + repr(y)

  #(x, y) = 2P
  #compute the inverse of 2P + P
  inverse = modInvEuclid((x - px)%n, n)
  multP = 2

  while(inverse != None):
    if(print_info):
      print "Inverse of " + repr((x - px)%n) + " is " + repr(inverse)
    #we don't have a factor - need to add P to (x,y)
    #compute Lamda - we'll use it outside of the if's to compute the new point
    lamda = ((y - py) * inverse) % n
    x = (lamda*lamda - px - x) % n
    y = (lamda * (px - x) - py) % n
    multP += 1
    if(print_info):
      print "no factor found - making next point"
      print "for " + repr(multP)+ "P: lamda = " + repr(lamda) + " new x = " + repr(x) + " new y = " + repr(y)
    #compute the next inverse
    inverse = modInvEuclid((x - px)%n, n)
  #we have found a factor - return it
  f = gcd(x - px, n)
  if(print_info):
    print "FOUND A FACTOR: " + repr(f)
  return f

      
      
def getLong(msg):
    try:
        data = long(raw_input(msg + " "))
    except ValueError:
        data = long(raw_input("Invalid input.  Try again: "))
    return data


def main():
    #get our value
    n = getLong("Input n, the value to factor: ")
    A = getLong("Input A, from the curve E: ")
    B = getLong("Input B, from the curve E: ")
    px = getLong("Input x, from the point you want to start with on E: ")
    py = getLong("Input y, from the point you want to start with on E: ")
    assert (py*py) % n == (px*px*px + A*px + B) % n
    f = factor(px, py, A, B, n, 1)

if __name__ == "__main__":
    main()
