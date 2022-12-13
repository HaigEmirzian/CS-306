#I pledge my honor that I have abided by the Stevens Honor System.
#Haig Emirzian

#Sophie Germain Lab Assignment #7

import random

#Checks to see if an input is prime
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

#Sees if Q and P are both prime
def SG(Q):
    P = (2*Q) + 1
    if is_prime(Q) == True and is_prime(P) == True:
        print("Q = " + str(Q) + " and P = " + str(P) + " are both prime.")
    else:
        print("Q needs to be a prime number.")

#Finds the smallest generator
def smallest_generator(Q):
    s = set(range(1, Q))
    results = []
    for i in s:
        g = set()
        for j in s:
            g.add((i**j) % Q)
        if g == s:
            results.append(i)
    return results[0]

#Checks to see if x^b(mod P) == y^a(mod P)
#a and b are random from Q
def DH(Q, P):
    if P == (2*Q) + 1:
        if is_prime(Q) == True and is_prime(P) == True:
            x = (smallest_generator(Q)**(random.randrange(Q + 1))) % P
            y = (smallest_generator(Q)**(random.randrange(Q + 1))) % P

            if ((x**(random.randrange(Q + 1))) % P) == ((y**(random.randrange(Q + 1))) % P):
                print("x^b(mod P) and y^a(mod P) are equal.")
            else:
                print("x^b(mod P) and y^a(mod P) are not equal.")
        else:
            print("Q and P need to be prime.")
    else:
        print("P needs to equal to 2*Q + 1.")
    
