import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
# AF_INET means addresses from the Internet.
# SOCK_DGRAM indicates that this will be a UDP client.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# send some data
# there is no need to call 'client.connect' because UDP is a connectionless protocol
client.sendto("AAABBBCCC",(target_host,target_port))

# receive some data
# recvfrom receives UDP data back and details of the remote host and port
data, addr = client.recvfrom(4096)

print data