import socket
import gmpy2

target_host = 'www.google.com'
target_port = 80
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to client
client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4092)

print(response)
