import socket
 
def Main():
        host = '127.0.0.1'
        port = 10000
         
        redSocket = socket.socket()
        redSocket.connect((host,port))
         
        message = input("Enter your role (defense/attack)\n -> ")
        
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                message = input(" -> ")
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
