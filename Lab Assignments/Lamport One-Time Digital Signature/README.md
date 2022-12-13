# Lamport One-Time Digital Signature Scheme

Lamport One-Time Digital Signature Scheme 

Let M = "any message" and d = digest(M) = digest of M using SHA256. 

(Sender) Key Generation: i) secret keys lists (matrix) sk[i][j] for all 0<=i<2 and 0<=j<256. (initialize with random numbers).

                             ii) generate public keys lists(matrix) pk[i][j] for all 0<=i<2 and 0<=j<256. (here, pk[i][j] = SHA256(sk[i][j]) for all 0<=i<2 and 0<=j<256.)

(Sender) DS Generation: i) For each d[i], the i(th) bit of digest d where 0<=i<256, ith block of digital signature DS[i] = sk[d[i]][i].

(Send M and DS to receiver)

(Receiver) DS Verification

                             i) From the received message, generate digest d' of 256 bits. (here, d'[i] is a bit for 0<=i<256)

                             ii) If (SHA256(DS[i])==pk[d'[i]][i]), DS is verified. Otherwise not verified.
