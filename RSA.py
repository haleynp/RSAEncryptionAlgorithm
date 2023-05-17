import random
import math


#Function to return a**b (mod n) where a, b, n are integers
#Returns the remainder when a**b is divided by n
#Implementation done mathematically without using pow()

def mod_power(a, b, n):
    powers_of_two = [1] 
    mods_of_two = [a % n]
    if mods_of_two[0] == 0:
        return 0
    answer = 1
    while powers_of_two[~0] < b:
        powers_of_two.append(powers_of_two[~0] * 2)
        mods_of_two.append(mods_of_two[~0]**2 % n)
    for i in range(len(powers_of_two)):
        if b >= powers_of_two[~i]:
            b -= powers_of_two[~i]
            answer = (answer*mods_of_two[~i]) % n
    return answer

def bezout_solver(a,b,k):
    r = [a, b]
    x = [1, 0]
    y = [0, 1]
    while r[~0] != 0:
        q = r[~1] // r[~0]
        r.append(r[~1]-q*r[~0])
        x.append(x[~1]-q*x[~0])
        y.append(y[~1]-q*y[~0])
    gcd = r[~1]
    if k % gcd != 0:
        return None, None, gcd
    else:
        c = k // gcd
        return c*x[~1], c*y[~1], r[~1]
    
def rsa_setup(p,q):
    n,e,d = 0, 0, 0
    n = p*q
    gcd = 0
    totient = (p-1)(q-1)
    e = 0
    for i in range(3, totient):
        gcd = math.gcd(i,totient)
        if(gcd == 1):
            e = i
    a, _, _ = bezout_solver(e,totient,1)
    d = mod_power(a, 1, totient)
    return n, e, d


def encrypt(n, e, message):
    return mod_power(message, e, n)

def decrypt(n, d, encrypted_message):
    return mod_power(encrypted_message, d, n)


    