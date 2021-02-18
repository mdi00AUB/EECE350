import socket
import datetime

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Create UDP Socket Object
serverAddress = ('127.0.0.1',3135) #localhost,port number tuple
sock.bind(serverAddress) #Bind server socket to address tuple

print("Server running on: ",  serverAddress) #Display server location


while True: #Keep socket open to recieve data
    data = sock.recvfrom(4096) #Recieve size
    if data:
        print(datetime.datetime.now()) #Display Date and Time of recieving
        print("Recieved from client: ", data[0].decode('utf-8')) #Decode and display recieved message
        sock.sendto(data[0],data[1]) #Send back the message to client address
sock.close() #close the socket

