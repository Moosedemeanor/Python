import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# pass in the IP address and port we want the server to listen on.
server.bind((bind_ip,bind_port))
# tell the server to start listening with a maximum backlog of connections set to 5
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# this client-handling thread function performs the recv() and then sends a simple message back to the client.
def handle_client(client_socket):

    # print out what the client sends
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request

    # send back a packet
    client_socket.send("I ACK YOU!")
    client_socket.close()
    
# we put the server into its main loop, where it is waiting for an incoming connection.
while True:
    # when a client connects we receive the client socket into the client variable, and the remote connection details into the addr variable. 
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
    # spin up our client thread to handle incoming data
    # we create a new thread object that points to our handle_client function, and we pass it the client socket object as an argument
    client_handler = threading.Thread(target=handle_client,args=(client,))
    # We then start the thread to handle the client connection, and our main server loop is ready to handle another incoming connection.
    client_handler.start()