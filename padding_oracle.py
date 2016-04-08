import requests

encoded = '48ed6188f9cea86ae4448777127a47ee06af170e4e08fd560c84bfc4fe25063a'
user = '56f6df17a189c615de24982e'
host = 'http://oracle.2016.volgactf.ru:7373/'
cookie = 'a07b097d0aea975f035846d39875f7b0'

def decode_block(block, prev_block):
    ret = ''
    m = [0] * 8
    for s in range(8):
        my_block_start = '0' * ((8 - s) * 2 - 2)
        my_block_end = ''
        for i in range(s):
            my_block_end = '0' * (2 - len(hex((s + 1) ^ m[7 - i])[2:])) + hex((s + 1) ^ m[7 - i])[2:] + my_block_end
        #print(my_block_start, my_block_end)
        for i in range(256):
            my_block = my_block_start + '0' * (2 - len(hex(i)[2:])) + hex(i)[2:] + my_block_end
            url = host + 'notes/' + user + '/' + my_block + block
            r = requests.get(url, cookies={'_la_tokionare': cookie})
            #print(r.text + hex(i))
            if r.json()['error'] != 'Invalid padding bytes.':
                t = i ^ (s + 1)
                m[7 - s] = t
                #print(t, prev_block[2 * (7 - s) : 2 * (7 - s) + 2])
                ret = chr(t ^ int(prev_block[2 * (7 - s) : 2 * (7 - s) + 2], 16)) + ret
                print(ret)
                break
    return ret

message = ''
for i in range(int(len(encoded) / 16) - 1):
    block = encoded[((len(encoded) - 16) - i * 16) : ((len(encoded) - 16) - i * 16) + 16]
    prev_block = encoded[((len(encoded) - 16) - i * 16) - 16 : ((len(encoded) - 16) - i * 16)]
    print(block, prev_block)
    message = decode_block(block, prev_block) + message
print(message)
