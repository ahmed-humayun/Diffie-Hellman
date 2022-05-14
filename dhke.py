from gmpy2 import mpz
from random import randrange, getrandbits

def mRT(p, s=3):
    
    # 2 and 3 are prime numbers
    if p == 2 or p == 3:
        return True
    
    # returns false for even numbers, 1, 0 and negative numbers
    elif p <= 1 or p % 2 == 0:
        return False
    
    # n - 1 = 2^u * r
    else:
        u = 0 
        r = p - 1
        
        #find u and r
        while r % 2 == 0:
            u += 1 
            r = r // 2
            
        # for s number of tests / witness loop
        for i in range (s):
             
            # random a between 2 and p-2
            a = randrange(2, p - 2)
            z = sq_and_mul(mpz(a), mpz(r), mpz(p))
            if z != 1 and z != p - 1:
                for j in range (u - 1):
                    z = sq_and_mul(mpz(z), 2, mpz(p))
                    if z == p - 1:
                        break
                if z == p - 1:
                    continue
                elif z != p - 1:
                    return False
        return True

def generate_prime(len=1024):
    while True:
        p = getrandbits(len)
         #set lsb to 1
        p = p | 1 << 0
        #set msb to 1
        p = p | 1 << len - 1 
        if mRT(p):
            break
    return p   
    
    
def sq_and_mul(x, h, n):
    bin_h = bin(h)
    y = x
    for i in (range(3, len(bin_h))):
        y = pow(y, 2, n)
        if int(bin_h[i]) == 1:
            y = (y * x) % n
    return y


def find_p_q(size = 1024):
    while True:
        prime = generate_prime(size)
        p = mpz((prime * 2) + 1)
        if mRT(p):
           q = prime
           prime = p
           break
    return prime, q
    

prime, q  = find_p_q()

print ("p:", prime, "\n")
print ("q:", q, "\n") 

print ("Prime Number: ", prime, "\n")
while True:
    generator = randrange(2, prime-2)
    if sq_and_mul(mpz(generator), 2, mpz(prime)) != 1 or sq_and_mul(mpz(generator), mpz(q), mpz(prime)) != 1:
        break
print("Generator: ", generator, "\n")

#secret keys
alice_secret = randrange(2, prime-1)
print("Alice Secret: ", alice_secret, "\n")
bob_secret = randrange(2, prime-1)
print("Bob Secret: ", bob_secret, "\n")

#partial keys
alice_partial_key = sq_and_mul(mpz(generator), mpz(alice_secret), mpz(prime)) 
print("Alice Partial Key: ", alice_partial_key, "\n")
bob_partial_key = sq_and_mul(mpz(generator), mpz(bob_secret), mpz(prime))
print("Bob Partial Key: ",bob_partial_key, "\n")

#final key
private_key_by_alice = sq_and_mul(mpz(bob_partial_key), mpz(alice_secret), mpz(prime))
print("Alice Private Key: ",private_key_by_alice, "\n")
private_key_by_bob = sq_and_mul(mpz(alice_partial_key), mpz(bob_secret), mpz(prime))
print("Bob Private Key: ",private_key_by_bob, "\n")

if mpz(private_key_by_alice) == mpz(private_key_by_bob):
    print("Alice and Bob has generated the same private key")
else:
    print("Alice and Bob has generated different private key")
