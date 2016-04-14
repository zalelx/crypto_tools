#!/usr/bin/python
from math import log
from math import trunc
import decimal
from Crypto.PublicKey import RSA

def convergents(cf):
    r, s, p, q = 0, 1, 1, 0
    for c in cf:
        r, s, p, q = p, q, c * p + r, c * q + s
        yield p, q


def contfrac(p, q):
    while q:
        n = p // q
        yield n
        q, p = p - q * n, q

def attack(idE, isN):
    
    limitD = (decimal.Decimal(n) * decimal.Decimal(0.33333333333333)).sqrt().sqrt()
    print ("Find D < 1/3*N^^1/4: D < " + str(limitD))
    
    myM = 0x01010101
    
    contf = list(convergents(contfrac(isE, isN)))
    for i in range(len(contf)):
        current = contf[i]
        if current[1] > limitD:
            break
        # C = M^^E mod N
        isC = pow(myM, isE, isN)
        # M = C^^D mod N
        myM2 = pow(isC, current[1], isN)
        if myM == myM2:
            print "VALID VALUE d =", current[1]
            return RSA.construct((isN, isE, current[1]))
        else:
            print "Can't find d exponent"
            return RSA.construct((isN, isE))

    

if __name__ == '__main__':
    with open('key.public', 'r') as f:
        key = RSA.importKey(f.read()) 
    with open('exit_key','w') as f:
        f.write(attack(key.e, key.n).exportKey("PEM"))

