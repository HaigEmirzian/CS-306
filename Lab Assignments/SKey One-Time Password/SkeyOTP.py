#Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#Name: Haig Emirzian

import hashlib
import secrets
import random

#S/Key One-Time Password
def OTP():
    K = "Hello World"
    n = random.randint(256, 2**16 - 1) 
    Hash = bin(int(hashlib.sha256(K.encode()).hexdigest(), 16))
    hashArr = [0 for i in range(n)]

    for i in range(n):
        hashArr[i] = Hash
        Hash = bin(int(hashlib.sha256(K.encode()).hexdigest(), 16)) 

    revArr = hashArr[::-1]
    Hash = bin(int(hashlib.sha256(K.encode()).hexdigest(), 16))
    clientArr = [0 for i in range(n)]

    for i in range(n):
        clientArr[i] = Hash
        Hash = bin(int(hashlib.sha256(Hash.encode()).hexdigest(), 16))

    clientReverse = clientArr[::-1]

    for i in range(n):
        match = True
        if(not clientReverse[i] == revArr[i]):
            match = False

    if(match):
        print("Authenticated")
    else:
        print("Not Authenticated")

print("S/Key One-Time Password")
print("|")
print("V")
OTP()
