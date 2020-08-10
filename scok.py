import socket

# create a socket object 

s = socket.socket()
print("#### Socket created successfuly")
# reserver a port 
port = 64444

# bind the port

s.bind(('',port))
print("## port is binded ")

# put the socket into listening mode 
s.listen(5)      
print ("## socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print ('Got connection from', addr)
  
   # send a thank you message to the client.  
   c.send(b"thanks send to client") 
  
   # Close the connection with the client 
   c.close() 