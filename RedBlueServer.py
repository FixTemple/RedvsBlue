# Programmer: Elliott Fix
#     Temple University, College of Engineering
# Start Date: December, 2016
# Version: 
# Code inspired by YoungsoonLee
#         https://github.com/YoungsoonLee/chatServer/blob/master/chat_server-eventlet.py
# Description: Server for multiple clients



import eventlet
import eventlet.queue as queue
import tincanchat
import module


HOST = tincanchat.HOST
PORT = tincanchat.PORT
send_queue = {}
status = True


def handle_client_recv(sock, addr):
    """ Receive messages from client and broadcast them to other clients until client disconnects """
    rest = bytes()
    red_turn = True
    map  = {'13': '', '23': '', '33': '',
            '12': '', '22': '', '32': '',
            '11': '', '21': '', '31': ''};
    while True:
        try:
            (msgs, rest) = tincanchat.recv_msgs(sock)
        except (EOFError, ConnectionError):
            handle_disconnect(sock, addr)
            break
        for msg in msgs:
            
            if (red_turn and msg[0]=='R'):
                print("RED MESSAGE")
                cord = msg[-2:]
                if (len(map[cord])==0):
                    map[cord] = 'R'
                    msg='M-'+cord+':R'
                else:
                    msg='M-'+cord+':B'
                red_turn = False   
                
            elif ((not red_turn) and msg[0]=='B'):      
                print("BLUE MESSAGE")
                red_turn = True
                cord = msg[-2:]
                if(len(map[cord])==0):
                    map[cord] = 'B'
                    msg='M-'+cord+':B'
                else:
                    msg='M-'+cord+':R'
                red_turn = True
            else:
                print("NOT VALID, WAIT YOUR TURN")
            
            broadcast_msg(msg)
            msg = '{}:{}'.format(addr, msg)
            print("\n--->" + msg)

def handle_client_send(sock, q, addr):
    """ Monitor queue for new messages, send them to client as they arrive """
    while True:
        msg = q.get()
        if not msg:
            break
        try:
            tincanchat.send_msg(sock, msg)
        except (ConnectionError, BrokenPipeError):
            handle_disconnect(sock, addr)
            break


def broadcast_msg(msg):
    """ Add message to each connected client's send queue """
    for q in send_queue.values():
        q.put(msg)


def handle_disconnect(sock, addr):
    """ Ensure queue is cleaned up and socket closed when a client disconnects """
    fd = sock.fileno()
    # Get send_queue for this client
    q = send_queue.get(fd, None)
    # If we find a queue then this disconnect has not yet
    # been handled
    if q:
        q.put(None)
        del send_queue[fd]
        addr = sock.getpeername()
        print('Client {} disconnected'.format(addr))
        status = False
        sock.close()


if __name__ == '__main__':
    server = eventlet.listen((HOST, PORT))
    addr = server.getsockname()
    print('Listening on {}'.format(addr))
    status = True

    while (status == True):
        client_sock, addr = server.accept()
        q = queue.Queue()
        send_queue[client_sock.fileno()] = q
        # TODO: see send_queue
        eventlet.spawn_n(handle_client_recv, client_sock, addr)
        eventlet.spawn_n(handle_client_send, client_sock, q, addr)
        print('Connection from {}'.format(addr))


