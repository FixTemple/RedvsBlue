# Programmer: Elliott Fix
# Temple University, College of Engineering
# Start Date: December, 2016
# Version: 0.1
# Code inspired by Shakeel Osmani
#        https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/
# Description: A basic CLient-Server program that features two client GUIs for
#              two players to compete in a game setting that models the attack
#              and defense of Internet security.


import socket

from afxres import AFX_IDC_COLOR_BLUE
 
def Red():
    host = "127.0.0.1"
    port = 10000
     
    redSocket = socket.socket()
    redSocket.bind((host,port))
     
    redSocket.listen(1)
    conn, addr = redSocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
                
            print ("sending: " + str(data))
            conn.send(data.encode())
            
    conn.close()

def Blue():
    host = "127.0.0.1"
    port = 10000
     
    blueSocket = socket.socket()
    blueSocket.bind((host,port))
     
    blueSocket.listen(1)
    conn, addr = blueSocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))   
                
            print ("sending: " + str(data))
            conn.send(data.encode())
                
             
    conn.close()
     
if __name__ == '__main__':
    Red()
    
#if __name__ == '__main__':
    #Blue()
