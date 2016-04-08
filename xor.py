from itertools import cycle, izip

message = '1c0111001f010100061a024b53535009181c'
key = '686974207468652062756c6c277320657965'
message = message.decode('hex')
key = key.decode('hex')

cyphered = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(message, cycle(key)))
print('%s ^ %s = %s' % (message, key, cyphered))
message = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(cyphered, cycle(key)))
print('%s ^ %s = %s' % (cyphered, key, message))

print(cyphered.encode('hex'))

