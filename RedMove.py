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


class RedMove(object):
    pointTotal = 0
    point11 = 20
    point12 = 40
    point13 = 50
    point21 = 10
    point22 = 20
    point23 = 50
    point31 = 20
    point32 = 40
    point33 = 50
    delayCost = 10
    sendAttackCost = 0
    max_grid_point = 33

    
    
    def __init__(self, master, queue, endCommand, sock):        
        self.redcolor = 'red'
        self.bluecolor = 'lightblue' 
        self.queue = queue
        height = 4
        width = 12
        self.sock = sock
        self.root=master
        self.create_winGUI(self.root, self.redcolor, height, width)

    
    def Color11(self):
        msg ='R-11'
        self.button_check_send(msg, self.pointTotal, self.point11)

    def Color12(self):
        msg ='R-12'
        self.button_check_send(msg, self.pointTotal, self.point12)

    def Color13(self):
        msg ='R-13'
        self.button_check_send(msg, self.pointTotal, self.point13)
        
    def Color21(self):
        msg ='R-21'
        self.button_check_send(msg, self.pointTotal, self.point21)

    def Color22(self):
        msg ='R-22'
        self.button_check_send(msg, self.pointTotal, self.point22)
        
    def Color23(self):
        msg ='R-23'
        self.button_check_send(msg, self.pointTotal, self.point23)
        
    def Color31(self):
        msg ='R-31'
        self.button_check_send(msg, self.pointTotal, self.point31)

    def Color32(self):
        msg ='R-32'
        self.button_check_send(msg, self.pointTotal, self.point32)
        
    def Color33(self):
        msg ='R-33'
        self.button_check_send(msg, self.pointTotal, self.point33)

        
    def DelayMove(self):
        self.pointTotal = self.move_delay(self.delayCost, self.pointTotal)
        self.label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        
    def SendAttack(self):
        msg = 'RA'
        self.button_check_send(msg, self.pointTotal, self.sendAttackCost)
        
    def testReset(self):
        self.pointTotal = 0
    
    
    def quit(self):
        msg ='q'
        tincanchat.send_msg(self.sock, msg)       
        self.root.destroy()     #Closes the GUI
        self.sock.close()       #Closes the socket, disconnects client
    
    
    def create_winGUI(self, root, redcolor, height, width):
        self.button11 = Button(root, text = self.point11, command = self.Color11, height=height, width=width)
        self.button12 = Button(root, text = self.point12, command = self.Color12, height=height, width=width, state = DISABLED)
        self.button13 = Button(root, text = self.point13, command = self.Color13, height=height, width=width, state = DISABLED)
        self.button21 = Button(root, text = self.point21, command = self.Color21, height=height, width=width)
        self.button22 = Button(root, text = self.point22, command = self.Color22, height=height, width=width, state = DISABLED)
        self.button23 = Button(root, text = self.point23, command = self.Color23, height=height, width=width, state = DISABLED)
        self.button31 = Button(root, text = self.point31, command = self.Color31, height=height, width=width)
        self.button32 = Button(root, text = self.point32, command = self.Color32, height=height, width=width, state = DISABLED)
        self.button33 = Button(root, text = self.point33, command = self.Color33, height=height, width=width, state = DISABLED)

        
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
        self.server_textbox = Text(root, height=height, width=3*width, padx=2, pady=2)
       
        #Define buttons
        self.buttonAttack = Button(root, text = 'Send\nAttack', command = self.SendAttack, height=height, width=width, state = DISABLED)
        self.buttonDelay = Button(root, text = "Delay\nMove", command = self.DelayMove, height=height, width=width)
        self.buttonQuit = Button(root, text = "Quit", command = self.quit, height=height, width=width, bg=self.redcolor)
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
        self.server_textbox.insert(INSERT, "From Server: ")
        self.button11.grid(row=3, column=1)
        self.button12.grid(row=2, column=1)
        self.button13.grid(row=1, column=1)
        self.button21.grid(row=3, column=2)
        self.button22.grid(row=2, column=2)
        self.button23.grid(row=1, column=2)
        self.button31.grid(row=3, column=3)
        self.button32.grid(row=2, column=3)
        self.button33.grid(row=1, column=3)
        self.buttonAttack.grid(row=1, column=5)
        self.buttonDelay.grid(row=2, column=5)
        self.buttonQuit.grid(row=5, column=5)
        self.testReset.grid(row=5, column=4)

        
    # Misc and Button Functions
 
    def process_incoming(self):    
        while self.queue.qsize():
            try:
                msg = self.queue.get(0).strip()
                cord=msg[-4:-2]
                print("From Server: " + msg)
                if (msg[0]=='M' and msg[-1:]=='R'):
                    self.label_turn.configure(text="Blue's turn")
                    self.root.update()
                    self.redraw(cord)
                    print(msg)
                    
                elif (msg[0]=='M' and msg[-1:]=='B'):
                    self.label_turn.configure(text="Red's turn")
                    self.root.update()
                
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
                    
                elif (msg[0]=='*' and msg[1]=='R'):
                    self.update_server_textbox(msg[3:32])
                
                else:
                    print("ERROR: Unidentified message")
                
            except queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass
            

    def button_check_send(self, msg, score, cost):
        if ( True ): ######### FIX THIS so that points aren't deducted when attempting to momve when it is not your turn
            message = msg
            tincanchat.send_msg(self.sock, message)
            self.pointTotal -= cost
            self.label_pointTotal.config(text = "Point Total: " + str(self.pointTotal)) 
        else:
            msg = "Invalid move; wait your turn!\n"
            self.update_server_textbox(msg)
 
 
    def redraw(self, cord):
        print("Current Location: " + cord)
        self.buttongroup[cord].configure(bg=self.redcolor)
        
        #convert the coordinate to an integer
        cord = int(cord)
        #check left coordinate availability
        if (cord-10 >= 11):
            self.buttongroup[str(cord-10)].configure(state = NORMAL)
            
        #check up and left availability    
        if (cord-9 >= 11 and cord-9 <= self.max_grid_point):
            self.buttongroup[str(cord-9 )].configure(state = NORMAL)
            
        #check right coordinate availability
        if (cord+10 <= self.max_grid_point):
            self.buttongroup[str(cord+10)].configure(state = NORMAL)
                        
        #check up and right coordinate availability
        if (cord+11 <= self.max_grid_point):
            self.buttongroup[str(cord+11)].configure(state = NORMAL)
            
        #check up availability
        if (cord+1 <= self.max_grid_point):
            self.buttongroup[str(cord+1 )].configure(state = NORMAL)
            
        #close blocks too far left
        if (cord-20 >= 11):
            self.buttongroup[str(cord-20)].configure(state = DISABLED)
            
        #close blocks too far up and left
        if (cord-19 >= self.max_grid_point):
            self.buttongroup[str(cord-19)].configure(state = DISABLED)
            
        #close blocks too far right
        if (cord+20 <= self.max_grid_point):
            self.buttongroup[str(cord+20)].configure(state = DISABLED)
            
        #close blocks too far up and right
        if (cord+21 <= self.max_grid_point):
            self.buttongroup[str(cord+21)].configure(state = DISABLED)
            
        #close blocks from grid row 3
        if ( (cord % 10) == 2 ):
            self.buttongroup['11'].configure(state = DISABLED)
            self.buttongroup['21'].configure(state = DISABLED)
            self.buttongroup['31'].configure(state = DISABLED)
        
        #close blocks from grid row 2    
        if ( (cord % 10) == 3 ):
            self.buttongroup['12'].configure(state = DISABLED)
            self.buttongroup['22'].configure(state = DISABLED)
            self.buttongroup['32'].configure(state = DISABLED)

        if (cord >= 20):
            self.buttonAttack.configure(state = NORMAL)
    
        self.label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        
        
    # Updates the server textbox by clearing text and printing the given message
    def update_server_textbox(self, msg):
        self.server_textbox.delete('1.0', END)
        self.server_textbox.insert(INSERT, "From Server:\n" + msg)
        self.root.update()
        
        
    # Function for the Delay Move button: Waits one turn, costs resources
    def move_delay(self, cost, score):
        if score < cost:
            msg = "Invalid Move", "You do not have enough resources!"
            self.update_server_textbox(msg)
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
    
    
