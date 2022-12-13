#Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#Name: Haig Emirzian

import hashlib
import secrets
import random

#creation of keys
def keygen():
    sk = [[0]*255, [1]*255]
    for i in range(len(sk)):
        for j in range(len(sk[i])):
            sk[i][j] = bin(secrets.randbits(255))[2:]
            sk[i][j] = '0'*(255-len(sk[i][j])) + sk[i][j]
    pk = [[0]*255, [1]*255]
    for i in range(len(pk)):
        for j in range(len(pk[i])):
            pk[i][j] = bin(int(hashlib.sha256(sk[i][j].encode()).hexdigest(), 16))
    keypair = [sk, pk]
    return keypair

#signature generation of the message
def signature(m, sk):
    hashed_message = int(hashlib.sha256(m.encode()).hexdigest(), 16)
    signature = [0]*255
    for i in range(255):
        j = int(bin(hashed_message >> i & 1)[2:])
        signature[i] = sk[j][i]
    return signature

# Verification of signature
def verify(m, pk, signature):
    hashed_message = int(hashlib.sha256(m.encode()).hexdigest(), 16)
    for i in range(255):
        j = int(bin(hashed_message >> i & 1)[2:])
        verify = bin(int(hashlib.sha256(str(signature[i]).encode()).hexdigest(), 16))
        if pk[j][i] != verify:
            return False
    return True

print("Lamport One-Time Digital Signature Scheme")
print("|")
print("V")
keypair = keygen()
m = "Hello World"
signature = signature(m, keypair[0])
result = print(verify(m, keypair[1], signature))
print("\n")
