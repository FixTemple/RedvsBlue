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


class BlueMove(object):
    pointTotal = 0
    point13 = 13
    point12 = 12
    point11 = 11
    point23 = 23
    point22 = 22
    point21 = 21
    point33 = 33
    point32 = 32
    point31 = 31
    delayCost = 10
    color = 'lightblue' 

    
    
    def __init__(self, master, queue, endCommand, sock):        
        self.queue = queue
        height = 4
        width = 12
        self.sock = sock
        self.root=master
        self.create_winGUI(self.root, self.color, height, width)

    
    def Color13(self):
        msg ='B-13'
        tincanchat.send_msg(self.sock, msg)
        
          
    def Color12(self):
        msg ='B-12'
        tincanchat.send_msg(self.sock, msg)

        
    def Color11(self):
        msg ='B-11'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color23(self):
        msg ='B-23'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color22(self):
        msg ='B-22'
        tincanchat.send_msg(self.sock, msg)
        
              
    def Color21(self):
        msg ='B-21'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color33(self):
        msg ='B-33'
        tincanchat.send_msg(self.sock, msg)

        
    def Color32(self):
        msg ='B-32'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color31(self):
        msg ='B-31'
        tincanchat.send_msg(self.sock, msg)
        
        
    def DelayMove(self):
        self.pointTotal = self.move_delay(self.delayCost, self.pointTotal)
        #label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        
    def pingRed(self):
        #Request red's location from server
        
        self.pointTotal = self.resource_check(self.pingCost, self.pointTotal)   
                     
        print (self.pointTotal)
        
    def testReset(self):
        self.pointTotal = 0
        
    def quit(self):
        msg ='q'
        tincanchat.send_msg(self.sock, msg)       
        self.root.destroy()     #Closes the GUI
        self.sock.close()       #Closes the socket, disconnects client
    
    
    def create_winGUI(self, root, color, height, width):
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
                             '12': self.button12 , '22': self.button22 , '23': self.button32,
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
        self.buttonPing = Button(root, text = 'Ping Red\nPosition', height=height, width=width, state = NORMAL)
        self.buttonDelay = Button(root, text = "Delay\nMove", command = self.DelayMove, height=height, width=width)
        self.buttonQuit = Button(root, text = "Quit", command = self.quit, height=height, width=width, bg=self.color)
        self.testReset = Button(root, text = "Test\nReset", command = self.testReset, height=height, width=width)
        
        #Align labels and buttons in grid
        self.label_x1.grid(row=0, column=1)
        self.label_x2.grid(row=0, column=2)
        self.label_x3.grid(row=0, column=3)
        self.label_y3.grid(row=1, column=0)
        self.label_y2.grid(row=2, column=0)
        self.label_y1.grid(row=3, column=0)
        self.label_pointTotal.grid(columnspan=4)
        self.label_turn.grid(row=4, columnspan=2)
        self.label_Actions.grid(row=0, column=5)
        self.server_textbox.grid(row=5, column=1, columnspan=3)
        self.server_textbox.insert(INSERT, "From Server: ")
#        self.server_textbox.configure(state=DISABLED)
        self.button13.grid(row=1, column=1)
        self.button12.grid(row=2, column=1)
        self.button11.grid(row=3, column=1)
        self.button23.grid(row=1, column=2)
        self.button22.grid(row=2, column=2)
        self.button21.grid(row=3, column=2)
        self.button33.grid(row=1, column=3)
        self.button32.grid(row=2, column=3)
        self.button31.grid(row=3, column=3)
        self.buttonDelay.grid(row=2, column=5)
        self.buttonQuit.grid(row=5, column=5)
        self.testReset.grid(row=5, column=4)

        
        
    def processIncoming(self):    
        while self.queue.qsize():
            try:
                msg = self.queue.get(0).strip()
                print("From Server: " + msg)
                if (msg[0]=='M' and msg[-1:]=='B'):
                    self.label_turn.configure(text="Red's turn")
                    self.root.update()
                    cord=msg[-4:-2]
                    self.redraw(cord)
                    print(msg)
                    
                elif (msg[0]=='M' and msg[-1:]=='R'):
                    self.label_turn.configure(text="Blue's turn")
                    self.root.update()
                
                elif (msg[0]=='M' and msg[-2:]=='BX'):
                    self.label_turn.configure(text="Blue's turn")
                    self.root.update()
                    print("Blocked by Blue")
                
                elif (msg[0]=='M' and msg[-2:]=='RX'):
                    self.label_turn.configure(text="Red's turn")
                    self.root.update()
                    print("Blocked by Red")

                else:
                    print(msg)
            except queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass
            
            
    def redraw(self, cord):
        print("Current Location: " + cord)
        self.buttongroup[cord].configure(bg=self.color)
        self.label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        

    def ping_red(self, cost, score):
        if score < cost:
            var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
        else:
            score = score - cost
            print ("Red was at position XXXX last turn")
            
                  
    def move_delay(self, cost, score):
        if score < cost:
            var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
        else:
            score = score - cost
            print ("Move Delayed")
        return score
    
    
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
            var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
        else:
            score = score - cost
            print (score)
        return score
    
    
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
    
    
