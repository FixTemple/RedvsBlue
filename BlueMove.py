# Programmer: Elliott Fix
#     Temple University, College of Engineering
# Start Date: December, 2016
# Version: 
# Code inspired by YoungsoonLee
#         https://github.com/YoungsoonLee/chatServer/blob/master/chat_server-eventlet.py
# Description: Client in Red vs Blue game



from tkinter import *
import tincanchat
from multiprocessing import Queue
import queue
from RedBlueServer import RedBlueServer


class BlueMove(object):
    pointTotal = 200
    point11 = 20
    point12 = 40
    point13 = 50
    point21 = 10
    point22 = 20
    point23 = 50
    point31 = 20
    point32 = 40
    point33 = 50
    pingCost = 60
    delayCost = 10
    bluecolor = 'lightblue'
    redcolor = 'red'
    redposition = ""
        
    #Button controls
    def __init__(self, master, queue, endCommand, sock):        
        self.queue = queue
        height = 4
        width = 12
        self.sock = sock
        self.root=master
        self.create_winGUI(self.root, self.bluecolor, height, width)

    def Color11(self):
        msg ='B-11'
        self.button_check_send(msg, self.pointTotal, self.point11)
                  
    def Color12(self):
        msg ='B-12'
        self.button_check_send(msg, self.pointTotal, self.point12)
        
    def Color13(self):
        msg ='B-13'
        self.button_check_send(msg, self.pointTotal, self.point13)
              
    def Color21(self):
        msg ='B-21'
        self.button_check_send(msg, self.pointTotal, self.point21)

    def Color22(self):
        msg ='B-22'
        self.button_check_send(msg, self.pointTotal, self.point22)

    def Color23(self):
        msg ='B-23'
        self.button_check_send(msg, self.pointTotal, self.point23)

    def Color31(self):
        msg ='B-31'
        self.button_check_send(msg, self.pointTotal, self.point31)
        
    def Color32(self):
        msg ='B-32'
        self.button_check_send(msg, self.pointTotal, self.point32)
        
    def Color33(self):
        msg ='B-33'
        self.button_check_send(msg, self.pointTotal, self.point33)

    def DelayMove(self):
        self.pointTotal = self.move_delay(self.delayCost, self.pointTotal)
        
    def pingRed(self):
        self.ping_red(self.pingCost, self.pointTotal)
        
    def testReset(self):
        self.pointTotal = 0
        
    def quit(self):
        msg ='q'
        tincanchat.send_msg(self.sock, msg)       
        self.root.destroy()     #Closes the GUI
        self.sock.close()       #Closes the socket, disconnects client
    
    
    def create_winGUI(self, root, bluecolor, height, width):
        self.button13 = Button(root, text = self.point13, command = self.Color13, height=height, width=width)
        self.button12 = Button(root, text = self.point12, command = self.Color12, height=height, width=width)
        self.button11 = Button(root, text = self.point11, command = self.Color11, height=height, width=width)
        self.button23 = Button(root, text = self.point23, command = self.Color23, height=height, width=width)
        self.button22 = Button(root, text = self.point22, command = self.Color22, height=height, width=width)
        self.button21 = Button(root, text = self.point21, command = self.Color21, height=height, width=width)
        self.button33 = Button(root, text = self.point33, command = self.Color33, height=height, width=width)
        self.button32 = Button(root, text = self.point32, command = self.Color32, height=height, width=width)
        self.button31 = Button(root, text = self.point31, command = self.Color31, height=height, width=width)
        
        self.buttongroup =  {'13': self.button13 , '23': self.button23 , '33': self.button33,
                             '12': self.button12 , '22': self.button22 , '32': self.button32,
                             '11': self.button11 , '21': self.button21 , '31': self.button31};
        
        #Assign text to labels
        self.label_x1 = Label(root, text = '1', height=height, width=width)
        self.label_x2 = Label(root, text = '2', height=height, width=width)
        self.label_x3 = Label(root, text = '3', height=height, width=width)
        self.label_y1 = Label(root, text = '1', height=height, width=width)
        self.label_y2 = Label(root, text = '2', height=height, width=width)
        self.label_y3 = Label(root, text = '3', height=height, width=width)
        self.label_pointTotal = Label(root, text = ("Point Total: " + str(self.pointTotal)), height=height, width=width)
        self.label_turn = Label(root, text = ("Red's Turn"), height=height, width=width)
        self.label_Actions = Label(root, text = 'Actions: ', height=height, width=width)
        self.server_textbox = Text(root, height=height, width=3*width, pady=2)
        
        #Define buttons
        self.buttonPing = Button(root, text = 'Ping Red\nPosition', command = self.pingRed, height=height, width=width, state = NORMAL)
        self.buttonDelay = Button(root, text = "Delay\nMove", command = self.DelayMove, height=height, width=width)
        self.buttonQuit = Button(root, text = "Quit", command = self.quit, height=height, width=width, bg=self.bluecolor)
        self.testReset = Button(root, text = "Test\nReset", command = self.testReset, height=height, width=width)
        
        #Align labels and buttons in grid
        self.label_x1.grid(row=0, column=1)
        self.label_x2.grid(row=0, column=2)
        self.label_x3.grid(row=0, column=3)
        self.label_y3.grid(row=1, column=0)
        self.label_y2.grid(row=2, column=0)
        self.label_y1.grid(row=3, column=0)
        self.label_pointTotal.grid(columnspan=4)
        self.label_turn.grid(row=4, column=0)
        self.label_Actions.grid(row=0, column=5)
        self.server_textbox.grid(row=5, column=0, columnspan=3)
        self.server_textbox.insert(INSERT, "From Server:\n")
        self.button13.grid(row=1, column=1)
        self.button12.grid(row=2, column=1)
        self.button11.grid(row=3, column=1)
        self.button23.grid(row=1, column=2)
        self.button22.grid(row=2, column=2)
        self.button21.grid(row=3, column=2)
        self.button33.grid(row=1, column=3)
        self.button32.grid(row=2, column=3)
        self.button31.grid(row=3, column=3)
        self.buttonPing.grid(row=1, column=5)
        self.buttonDelay.grid(row=2, column=5)
        self.buttonQuit.grid(row=5, column=5)
        self.testReset.grid(row=5, column=4)

        
    #Misc and Button Functions
    def button_check_send(self, msg, score, cost):
        if (score > cost):
            if (self.resource_check(cost, score)):
                message = msg
                tincanchat.send_msg(self.sock, message)
            else:
                return False
        else:
            self.update_server_textbox(msg)
            
        
    def process_incoming(self):    
        while self.queue.qsize():
            try:
                msg = self.queue.get(0).strip()
                print("From Server: " + msg)
                cord=msg[-4:-2]
                if (msg[0]=='M' and msg[-1:]=='B'):
                    self.label_turn.configure(text="Red's turn")
                    self.pointTotal -= int(self.buttongroup[cord].text)
                    self.label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
                    self.root.update()
                    self.redraw(cord)
                    print(msg)
                    
                elif (msg[0]=='M' and msg[-1:]=='R'):
                    self.label_turn.configure(text="Blue's turn")
                    self.root.update()
                    self.redposition = msg[2:4]
                    self.update_score(msg, self.pointTotal)
                                    
                elif (msg[0]=='M' and msg[-2:]=='BX'):
                    self.label_turn.configure(text="Blue's turn")
                    self.root.update()
                    msg = "Blocked by Blue"
                    self.buttongroup[cord].configure(bg = self.bluecolor)
                    self.update_server_textbox(msg)
                
                elif (msg[0]=='M' and msg[-2:]=='RX'):
                    self.label_turn.configure(text="Red's turn")
                    self.root.update()
                    msg = "Blocked by Red"
                    self.buttongroup[cord].configure(bg = self.redcolor)
                    self.update_server_textbox(msg)
                    
                elif (msg[0]=='*' and msg[1]=='B'):
                    self.update_server_textbox(msg[3:31])
                    
                else:
                    print("ERROR: Unidentified Message")
                    
            except queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass
    
    
    def redraw(self, cord):
        print("Current Location: " + cord)
        self.buttongroup[cord].configure(bg=self.bluecolor)
        self.label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        self.root.update()
        
        
    def update_server_textbox(self, msg):
        self.server_textbox.delete('1.0', END)
        self.server_textbox.insert(INSERT, "From Server:\n" + msg)
        self.root.update()
        
    def update_score(self, msg, score):
        print(msg)
#        score = score - cost
        self.label_pointTotal.config(text = "Point Total: " + str(score))
        print (score)
        

    def ping_red(self, cost, score):
#        if (self.redposition) = "":
        if (self.resource_check(cost, score)):
            score = score - cost
            msg = "Red was at position " + self.redposition + " last turn."
            self.update_server_textbox(msg)
#        else
#            msg = "Invalid Move: Wait your turn!"
            
                  
    def move_delay(self, cost, score):
        if (self.resource_check(cost, score)):
            print ("Move Delayed")
            ################### MAKE A MOVE DELAY FUNCTION
        return True
    
    
    def add_points(self, value, score):
        score = score + value
        return score
    
    
    def button_data_send(self, msg, sock, rest):
        try:
            print(type(sock))
            # blocks
            (msgs, rest) = tincanchat.recv_msgs(sock, rest)
            for msg in msgs:
                print(msg)
        except ConnectionError:
            print('Connection to server closed')
            sock.close()
            #break
    
    
    def resource_check(self, cost, score):
        if score < cost:
            msg = "Invalid Move", "You do not have enough resources!"
            self.update_server_textbox(msg)
            return False
        else:
            return True
    
    
    def handle_input(self, sock):
        """ Prompt user for message and send it to server """
        print("Type messages, enter to send. 'q' to quit")
        while True:
            msg = input()  # blocks
            if msg == 'q':
                # sock.shutdown(socket.SHUT_RDWR)
                sock.close()
                break
            try:
                tincanchat.send_msg(sock, msg)  # blocks until sent
            except (BrokenPipeError, ConnectionError):
                break

    
