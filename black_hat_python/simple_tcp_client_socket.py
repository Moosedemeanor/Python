import socket

target_host = "127.0.0.1"
target_port = 9999

# create a socket object
# AF_INET means addresses from the Internet.
# SOCK_STEAM indicates that this will be a TCP client.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to the server
client.connect((target_host,target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

# print out the received data
print response

# this script assumes that:
# your connection will always succeed.
# the server is always expecting us to send data first (as opposed to servers that expect to send data to you first and await your response). 
# the server will always send us data back in a timely fashion. 