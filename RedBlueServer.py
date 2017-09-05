# Programmer: Elliott Fix
#     Temple University, College of Engineering
# Start Date: December, 2016
# Version: 
# Code inspired by YoungsoonLee
#         https://github.com/YoungsoonLee/chatServer/blob/master/chat_server-eventlet.py
# Description: Server for two clients in Red vs Blue



import eventlet
import eventlet.queue as queue
import tincanchat
from imp import reload
import unittest


class RedBlueServer:
    HOST = tincanchat.HOST
    PORT = tincanchat.PORT
    send_queue = {}
    red_turn = True
    grid_map  = {'13': '', '23': '', '33': '',
                 '12': '', '22': '', '32': '',
                 '11': '', '21': '', '31': ''};
    
    
    def __init__(self):
    
        server = eventlet.listen((self.HOST, self.PORT))
        addr = server.getsockname()
        print('Listening on {}'.format(addr))
    
        while True:
            client_sock, addr = server.accept()
            q = queue.Queue()
            self.send_queue[client_sock.fileno()] = q
            eventlet.spawn_n(self.handle_client_recv, client_sock, addr)
            eventlet.spawn_n(self.handle_client_send, client_sock, q, addr)
            print('Connection from {}'.format(addr))
            
    def handle_client_recv(self, sock, addr):
        # Receive messages from client and broadcast them to other clients until client disconnects
        rest = bytes()
    
        while True:
            try:
                (msgs, rest) = tincanchat.recv_msgs(sock)
            except (EOFError, ConnectionError):
                self.handle_disconnect(sock, addr)
                break
            red_turn = self.red_turn
            grid_map = self.grid_map
            for msg in msgs:
                print("Update: red_turn value is ")
                print(red_turn)
                
                if (msg[0]=='R' and red_turn):
                    print("\nRED MESSAGE")
                    cord = msg[-2:]
                    if (red_turn):
                        if (len(grid_map[cord])==0):
                            self.grid_map[cord] = 'R'
                            msg='M-'+cord+':R'                                  # R:  New verified coordinate of Red's position
                        else:
                            msg='M-'+cord+'BX'                                  # BX: Blue has blocked this position
                        self.red_turn = False
                        self.broadcast_msg(msg)
                        msg = '{}:{}'.format(addr, msg)
                        print("--->" + msg )
                    else:
                        msg = '* Not a valid move; wait your turn!'
                        msg = '{}:{}'.format(addr, msg)
                        print("--->" + msg)
                        self.red_turn = False
                        self.broadcast_msg(msg)
                    print(self.red_turn)
                    print('\n\n')
                    
                elif (msg[0]=='B' and not red_turn):      
                    print("\nBLUE MESSAGE")
                    cord = msg[-2:]
                    if (not red_turn):
                        if(len(grid_map[cord])==0):
                            self.grid_map[cord] = 'B'
                            msg='M-'+cord+':B'                                  # B:  New verified coordinate of Blue's position
                        else:
                            msg='M-'+cord+'RX'                                  # RX: Red has blocked this position
                        self.red_turn = True
                        self.broadcast_msg(msg)
                    else:
                        msg = '* Not a valid move; wait your turn!'
                        #msg = '{}:{}'.format(addr, msg)
                        #print("--->" + msg)
                        #self.red_turn = True
                        self.broadcast_msg(msg)
                    print(self.red_turn)
                    msg = '{}:{}'.format(addr, msg)
                    print("--->" + msg)
                    print('\n\n')
                    
                elif (msg[0]=='R' and not red_turn):
                    msg = "*R Invalid Move: Wait your turn!"
                    self.broadcast_msg(msg)
                    
                elif (msg[0]=='B' and red_turn):
                    msg = "*B Invalid Move: Wait your turn!"
                    self.broadcast_msg(msg)
                    
                else:
                    print("ERROR: Unidentified Message")
    
    def handle_client_send(self, sock, q, addr):
        """ Monitor queue for new messages, send them to client as they arrive """
        while True:
            msg = q.get()
            if not msg:
                break
            try:
                tincanchat.send_msg(sock, msg)
            except (ConnectionError, BrokenPipeError):
                self.handle_disconnect(sock, addr)
                break
    
    
    def broadcast_msg(self, msg):
        """ Add message to each connected client's send queue """
        for q in self.send_queue.values():
            q.put(msg)
    
    
    def handle_disconnect(self, sock, addr):
        """ Ensure queue is cleaned up and socket closed when a client disconnects """
        # Reset the turn counter
        self.red_turn = True
        
        fd = sock.fileno()
        # Get send_queue for this client
        q = self.send_queue.get(fd, None)
        # If we find a queue then this disconnect has not yet been handled
        if q:
            q.put(None)
            del self.send_queue[fd]
            addr = sock.getpeername()
            print('Client {} disconnected'.format(addr))
            sock.close()
            #os.execl(sys.executable, sys.executable, *sys.argv).               #Restart program?
            #reload(self.__init__)

    

if __name__ == '__main__':
    
    #unittest.RedBlueServer()
    newserver = RedBlueServer()
    
