# RSA

Generate/Verify Digital Signature for a message using RSA. Use the following steps:

RSA Key Generation:

        1. Find random primes P and Q in the range(2^31 and 2^32-1).

        2. Calculate N = P *Q

        3. Phi(N) = (P-1)*(Q-1)

        4. Select (random) e such that 1<e<Phi(N) and gcd(e, Phi(N))=1.

        5. Calculate d such that e*d = 1(mod Phi(N))

Digital Signature Generation by Sender:

        1. Message M

        2. Use SHA256 to find the digest of M (digest_60 = first 60 bits of digest).

        3. Generate digital signature, DS = digest_60^d (mod N).

        4. Send M and DS to receiver.

Digital Signature Verification by Reciever:

       1. Received message = M' and digital signature = DS'.

       2. Use SHA256 to find the digest of M' (digest_60 = first 60 bits of digest).

       3. If digest_60 and (DS')^e (mod N) are equal, M' is signed by sender. Otherwise, signature DS' is invalid.
