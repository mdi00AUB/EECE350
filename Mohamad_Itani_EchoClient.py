import socket
import time

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#Create UDP Socket Object
serverAddress = ('127.0.0.1', 3135) #localhost, port number tuple


msg = "Echo Request"
RTTs = [0,0,0,0,0] #List to store RTTs
i=0
while i<=4: #5 iterations
    start_time = time.time()
    client.sendto(msg.encode('utf-8'),serverAddress) #send encoded message to server
    data = client.recvfrom(4096)
    print("Recieved from server: ", data[0].decode('utf-8')) #Print recieved message
    end_time = time.time()
    RTT = (end_time-start_time)*1000 #RTT in milliseconds
    RTTs[i] = RTT #store RTT for i'th iteration
    print("RTT = ",round(RTT,5),"milliseconds") #print RTT for i'th iteration
    i+=1
Avg = (RTTs[0]+RTTs[1]+RTTs[2]+RTTs[3]+RTTs[4])/5 #Avg RTT
print("Average RTT is: ", Avg, "milliseconds")

client.close() #Close the socket

