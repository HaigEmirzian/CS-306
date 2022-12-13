# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Name: Haig Emirzian

import hashlib
import math
import random

# Checks to see if a number is prime
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    
    i = 5
    stop = int(n**0.5)
    
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

# finds GCD
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
# a is phiN and b is e
def Extended_Euclidean_Algorithm(a,b):
    if a%b == 0 : #when b divides a
        return b,0,1
    gcd,x1,y1 = Extended_Euclidean_Algorithm(b, a%b)
    # Update x and y using results of recursive call
    x = y1
    y = x1 - (a//b) * y1
    return gcd,x,y

def key_generation_RSA():
    P = random.randint(pow(2,31), pow(2,32) - 1)

    while True:
        if is_prime(P) == True:
            break
        else:
            P = random.randint(pow(2,31), pow(2,32) - 1)

    Q = random.randint(pow(2,31), pow(2,32) - 1)

    while True:
        if is_prime(Q) == True:
            break
        else:
            Q = random.randint(pow(2,31), pow(2,32) - 1)

    if P >= pow(2,31) and Q >= pow(2,31) and P < pow(2, 32) and Q < pow(2, 32):
        pass
    else:
        raise Exception("P and Q should be >= to 2^31 and < 2^32.")
    
    N = P * Q

    phiN = (P - 1) * (Q - 1)

    e = random.randint(2, phiN - 1)

    if(find_gcd(e, phiN) == 1):
        gcd, x, y = Extended_Euclidean_Algorithm(e, phiN)
        message = "Hello World"
        digest = int(hashlib.sha256(message.encode('utf-8')).hexdigest(), 16)
        digest = bin(digest)[0:61]
        DS = pow(int(digest, 2), x, N)
        var = pow(DS, e, N)
        
        print(bin(var))
        print(digest)

        if digest == bin(var):
            print("Messages are equal.")
            print("The message is: " + message + ".")
        
        #returns d
        #x = d
        return e, x, N
    else:
        print("Messages are not equal.")
    
key_generation_RSA()    
