#!/usr/bin/python
from math import log
from math import trunc
from Crypto.PublicKey import RSA

#with open('key.public', 'r') as f:
    #key = RSA.importKey(f.read())

e = 5293075057801716664367463246933281029649537277618783295146296429087863857475871584611314658278591964724726817220973548583614292848383496273161085119696263
n = 89289569749693772955196197756934391863965025474824742350856665318955794595982874405284996032431520230637086068279468331020105227536913678363470893335097612798241155221587475664594428479535592339253219502514866422642810566128653904523545493563370798812012226996825197881178366004671709160608086305928029624053


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


isE = e
isN = n
print e
print n

limitD = int(pow(0.33 * isN, 0.25))
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
        print ("is fraction: " + str(current[0]) + "/" + str(current[1]) +
               ". Need check denominator: " + str(current[1]) + ". VALID VALUE")
    else:
        print ("is fraction: " + str(current[0]) + "/" + str(current[1]) +
               ". Need check denominator: " + str(current[1]) + ". Invalid")

#if __name__ == '__main__':
 #   tup = (n,e,d)
  ## with open('ciphertext.bin', 'rb') as f:
    #    C = f.read()
    #print key.decrypt(C)

