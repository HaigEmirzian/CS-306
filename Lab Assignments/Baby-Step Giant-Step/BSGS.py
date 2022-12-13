#Name: Haig Emirzian
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.

from math import ceil
from math import sqrt

def BSGS(b, g, p):
    
    m = ceil(sqrt(p - 1))  
    baby =[]
    
    for i in range(m):
       baby.append(pow(g, i, p))
       

    FLT = pow(g, m * (p - 2), p)

    for j in range(m):
        k = (b * pow(FLT, j, p)) % p
        if k in baby:
            return m * j + baby[j]
