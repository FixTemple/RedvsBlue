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
             
            if data == "attack":
                data = "You are red team"
            elif data == "defense":
                data = "You are blue team"
            else:
                print ("Please enter only attack or defense")    
                
            print ("sending: " + str(data))
            conn.send(data.encode())
                
             
    conn.close()
     
if __name__ == '__main__':
    Red()
    
#if __name__ == '__main__':
    #Blue()
