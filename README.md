# Diffie-Hellman Key Exchange Implementation

This project is an implementation of the Diffie-Hellman key exchange algorithm in Python. The Diffie-Hellman key exchange is a method for securely exchanging keys over a public channel. It allows two parties to establish a shared secret key, which can be used for encryption or authentication, without the need for one party to share their secret key with the other party.

The code uses the Miller-Rabin primality test (mRT()) to generate large prime numbers. The function generate_prime() generates a random prime number of a specified length, and the function find_p_q() finds two prime numbers, p and q, such that p=2q+1. The code then chooses a generator g randomly between 2 and p-2 and generates two secret keys for Alice and Bob. Alice and Bob then compute partial keys by raising the generator to the power of their secret keys modulo p. The final key is computed by raising the other party's partial key to the power of the own secret key modulo p. In this implementation, the function sq_and_mul() is used to perform modular exponentiation. This is a more efficient method of performing exponentiation in modulo than using pow(). The function takes in three arguments, a base x, an exponent h and a modulus n, and returns x^h mod n.
