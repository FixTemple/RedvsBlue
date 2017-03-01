from tkinter import *
import tincanchat
from module import add_points
from multiprocessing import Queue
from Queue import Empty


class RedMove(object):
    pointTotal = 0
    point1A = 70
    point1B = 40
    point1C = 10
    point2A = 80
    point2B = 50
    point2C = 20
    point3A = 90
    point3B = 60
    point3C = 30
    delayCost = 10

    
    
    def __init__(self, master, queue, endCommand, sock):        
        self.color = 'red' 
        self.queue = queue
        height = 4
        width = 12
        self.sock = sock
        self.root=master
        self.create_winGUI(self.root, self.color, height, width)

    
    def Color1A(self):
        msg ='R-13'
        tincanchat.send_msg(self.sock, msg)
        
          
    def Color1B(self):
        msg ='R-12'
        tincanchat.send_msg(self.sock, msg)

        
    def Color1C(self):
        msg ='R-11'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color2A(self):
        msg ='R-23'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color2B(self):
        msg ='R-22'
        tincanchat.send_msg(self.sock, msg)
        
              
    def Color2C(self):
        msg ='R-21'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color3A(self):
        msg ='R-33'
        
        
    def Color3B(self):
        msg ='R-32'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color3C(self):
        msg ='R-31'
        tincanchat.send_msg(self.sock, msg)
        
        
    def DelayMove(self):
        self.pointTotal = module.move_delay(self.delayCost, self.pointTotal)
        label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        
        
    def testReset(self):
        self.pointTotal = 0
        button1A.configure(state = DISABLED, bg='gray95')
        button1B.configure(state = DISABLED, bg='gray95')
        button1C.configure(state = NORMAL, bg='gray95')
        button2A.configure(state = DISABLED, bg='gray95')
        button2B.configure(state = DISABLED, bg='gray95')
        button2C.configure(state = NORMAL, bg='gray95')
        button3A.configure(state = DISABLED, bg='gray95')
        button3B.configure(state = DISABLED, bg='gray95')
        button3C.configure(state = NORMAL, bg='gray95')
        label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
    
    
    def quit(self):
        msg ='q'
        tincanchat.send_msg(self.sock, msg)       
        self.root.destroy()     #Closes the GUI
        self.sock.close()       #Closes the socket, disconnects client
    
    
    def create_winGUI(self, root, color, height, width):
        self.button13 = Button(root, text = self.point1A, command = self.Color1A, height=height, width=width, state = DISABLED)
        self.button12 = Button(root, text = self.point1B, command = self.Color1B, height=height, width=width, state = DISABLED)
        self.button11 = Button(root, text = self.point1C, command = self.Color1C, height=height, width=width)
        self.button23 = Button(root, text = self.point2A, command = self.Color2A, height=height, width=width, state = DISABLED)
        self.button22 = Button(root, text = self.point2B, command = self.Color2B, height=height, width=width, state = DISABLED)
        self.button21 = Button(root, text = self.point2C, command = self.Color2C, height=height, width=width)
        self.button33 = Button(root, text = self.point3A, command = self.Color3A, height=height, width=width, state = DISABLED)
        self.button32 = Button(root, text = self.point3B, command = self.Color3B, height=height, width=width, state = DISABLED)
        self.button31 = Button(root, text = self.point3C, command = self.Color3C, height=height, width=width)
        
        self.buttongroup =  {'13': self.button13 , '23': self.button23 , '33': self.button33,
                             '12': self.button12 , '22': self.button22 , '32': self.button32,
                             '11': self.button11 , '21': self.button21 , '31': self.button31};
        
        #Assign text to labels
        self.label_x1 = Label(root, text = '1', height=height, width=width)
        self.label_x2 = Label(root, text = '2', height=height, width=width)
        self.label_x3 = Label(root, text = '3', height=height, width=width)
        self.label_y3 = Label(root, text = '3', height=height, width=width)
        self.label_y2 = Label(root, text = '2', height=height, width=width)
        self.label_y1 = Label(root, text = '1', height=height, width=width)
        self.label_pointTotal = Label(root, text = "Point Total: " + str(self.pointTotal), height=height, width=width)
        self.label_Actions = Label(root, text = 'Actions: ', height=height, width=width)
        #label_Server = Label(root, text = "From Server: " + str(msg), height=height, width=width)
        
        #Define buttons
        self.buttonAttack = Button(root, text = 'Send\nAttack', height=height, width=width, state = DISABLED)
        self.buttonDelay = Button(root, text = "Delay\nMove", command = self.DelayMove, height=height, width=width)
        self.buttonQuit = Button(root, text = "Quit", command = self.quit, height=height, width=width)
        self.testReset = Button(root, text = "Test\nReset", command = self.testReset, height=height, width=width)
        
        #Align labels and buttons in grid
        self.label_x1.grid(row=0, column=1)
        self.label_x2.grid(row=0, column=2)
        self.label_x3.grid(row=0, column=3)
        self.label_y3.grid(row=1, column=0)
        self.label_y2.grid(row=2, column=0)
        self.label_y1.grid(row=3, column=0)
        self.label_pointTotal.grid(columnspan=4)
        #label_Server.grid(columnspan=3)
        self.label_Actions.grid(row=0, column=5)
        self.button13.grid(row=1, column=1)
        self.button12.grid(row=2, column=1)
        self.button11.grid(row=3, column=1)
        self.button23.grid(row=1, column=2)
        self.button22.grid(row=2, column=2)
        self.button21.grid(row=3, column=2)
        self.button33.grid(row=1, column=3)
        self.button32.grid(row=2, column=3)
        self.button31.grid(row=3, column=3)
        self.buttonAttack.grid(row=1, column=5)
        self.buttonDelay.grid(row=2, column=5)
        self.buttonQuit.grid(row=5, column=4)
        self.testReset.grid(row=5, column=3)
        
 
    def processIncoming(self):    
        while self.queue.qsize():
            try:
                msg = self.queue.get(0).strip()
                print("From Server: " + msg)
                if (msg[0]=='M' and msg[-1:]=='B'):
                    print("illegal move")
                else:
                    cord=msg[-4:-2]
                    self.redraw(cord)
            except Queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass
            

    def redraw(self, cord):
        print("Current Location: " + cord)
        self.buttongroup[cord].configure(bg=self.color)
        #check left coordinate availability
        if (cord-10 > 0):
            self.buttongroup[cord-10].configure(state = NORMAL)
        #check right coordinate availability
        if (cord+10 < 40):
            self.buttongroup[cord+10].configure(state = NORMAL)
            
        #check up and left availability    
        if (cord-9 < 40):
            self.buttongroup[cord-9].configure(state = NORMAL)
            
        #check up availability
        if (cord+1 < 40):
            self.buttongroup[cord+1].configure(state = NORMAL)
        #check up and right coordinate availability
        if (cord+11 < 40):
            self.buttongroup[cord+11].configure(state = NORMAL)
        
        self.pointTotal = add_points(self.point1C, self.pointTotal)
        self.label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        
    def update_gui(self, cord):
        if (cord == '11'):
            self.buttongroup[cord].configure
                  
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
    
    
