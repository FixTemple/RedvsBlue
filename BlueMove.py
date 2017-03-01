from tkinter import *
import tincanchat
from module import add_points
from multiprocessing import Queue


class BlueMove(object):
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
        self.color = 'lightblue' 
        self.queue = queue
        height = 4
        width = 12
        self.sock = sock
        self.root=master
        self.create_winGUI(self.root, self.color, height, width)

    
    def Color1A(self):
        msg ='B-1A'
        tincanchat.send_msg(self.sock, msg)
        
          
    def Color1B(self):
        msg ='B-1B'
        tincanchat.send_msg(self.sock, msg)

        
    def Color1C(self):
        msg ='B-1C'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color2A(self):
        msg ='B-2A'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color2B(self):
        msg ='B-2B'
        tincanchat.send_msg(self.sock, msg)
        
              
    def Color2C(self):
        msg ='B-2C'
        tincanchat.send_msg(self.sock, msg)
        
    def Color3A(self):
        button3A.configure(bg=color)
        self.pointTotal = module.add_points(self.point3A, self.pointTotal)
        print (self.pointTotal)
        label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        button3A.configure(state = DISABLED)
        button2A.configure(state = NORMAL)
        button1A.configure(state = DISABLED)
        button1B.configure(state = DISABLED)
        button3B.configure(state = DISABLED)
        button2B.configure(state = DISABLED)
        buttonAttack.configure(state = NORMAL)
        
        msg ='R-A:3A'
        
    def Color3B(self):
        msg ='B-3B'
        tincanchat.send_msg(self.sock, msg)
        
        
    def Color3C(self):
        msg ='B-3C'
        tincanchat.send_msg(self.sock, msg)
        
    def DelayMove(self):
        self.pointTotal = self.move_delay(self.delayCost, self.pointTotal)
        #label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        
    def pingRed(self):
        #Request red's location from server
        
        self.pointTotal = self.resource_check(self.pingCost, self.pointTotal)   
                     
        print (self.pointTotal)
        #label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
        #make label for red pinged position
        
    def testReset(self):
        self.pointTotal = 0
        button1A.configure(state = NORMAL, bg='gray95')
        button1B.configure(state = NORMAL, bg='gray95')
        button1C.configure(state = NORMAL, bg='gray95')
        button2A.configure(state = NORMAL, bg='gray95')
        button2B.configure(state = NORMAL, bg='gray95')
        button2C.configure(state = NORMAL, bg='gray95')
        button3A.configure(state = NORMAL, bg='gray95')
        button3B.configure(state = NORMAL, bg='gray95')
        button3C.configure(state = NORMAL, bg='gray95')
        label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
    
    def quit(self):
        msg ='q'
        tincanchat.send_msg(self.sock, msg)       
        self.root.destroy()     #Closes the GUI
        self.sock.close()       #Closes the socket, disconnects client
    
    
    def create_winGUI(self, root, color, height, width):
        self.button1A = Button(root, text = self.point1A, command = self.Color1A, height=height, width=width, state = DISABLED)
        self.button1B = Button(root, text = self.point1B, command = self.Color1B, height=height, width=width, state = DISABLED)
        self.button1C = Button(root, text = self.point1C, command = self.Color1C, height=height, width=width)
        self.button2A = Button(root, text = self.point2A, command = self.Color2A, height=height, width=width, state = DISABLED)
        self.button2B = Button(root, text = self.point2B, command = self.Color2B, height=height, width=width, state = DISABLED)
        self.button2C = Button(root, text = self.point2C, command = self.Color2C, height=height, width=width)
        self.button3A = Button(root, text = self.point3A, command = self.Color3A, height=height, width=width, state = DISABLED)
        self.button3B = Button(root, text = self.point3B, command = self.Color3B, height=height, width=width, state = DISABLED)
        self.button3C = Button(root, text = self.point3C, command = self.Color3C, height=height, width=width)
        
        self.buttongroup =  {'1A': self.button1A , '2A': self.button2A , '3A': self.button3A,
                             '1B': self.button1B , '2B': self.button2B , '3B': self.button3B,
                             '1C': self.button1C , '2C': self.button2C , '3C': self.button3C};
        
        #Assign text to labels
        self.label_1 = Label(root, text = '1', height=height, width=width)
        self.label_2 = Label(root, text = '2', height=height, width=width)
        self.label_3 = Label(root, text = '3', height=height, width=width)
        self.label_A = Label(root, text = 'A', height=height, width=width)
        self.label_B = Label(root, text = 'B', height=height, width=width)
        self.label_C = Label(root, text = 'C', height=height, width=width)
        self.label_pointTotal = Label(root, text = "Point Total: " + str(self.pointTotal), height=height, width=width)
        self.label_Actions = Label(root, text = 'Actions: ', height=height, width=width)
        #label_Server = Label(root, text = "From Server: " + str(msg), height=height, width=width)
        
        #Define buttons
        self.buttonPing = Button(root, text = 'Ping Red\nPosition', height=height, width=width, state = NORMAL)
        self.buttonDelay = Button(root, text = "Delay\nMove", command = self.DelayMove, height=height, width=width)
        self.buttonQuit = Button(root, text = "Quit", command = self.quit, height=height, width=width)
        self.testReset = Button(root, text = "Test\nReset", command = self.testReset, height=height, width=width)
        
        #Align labels and buttons in grid
        self.label_1.grid(row=0, column=1)
        self.label_2.grid(row=0, column=2)
        self.label_3.grid(row=0, column=3)
        self.label_A.grid(row=1, column=0)
        self.label_B.grid(row=2, column=0)
        self.label_C.grid(row=3, column=0)
        self.label_pointTotal.grid(columnspan=4)
        #label_Server.grid(columnspan=3)
        self.label_Actions.grid(row=0, column=5)
        self.button1A.grid(row=1, column=1)
        self.button1B.grid(row=2, column=1)
        self.button1C.grid(row=3, column=1)
        self.button2A.grid(row=1, column=2)
        self.button2B.grid(row=2, column=2)
        self.button2C.grid(row=3, column=2)
        self.button3A.grid(row=1, column=3)
        self.button3B.grid(row=2, column=3)
        self.button3C.grid(row=3, column=3)
        self.buttonAttack.grid(row=1, column=5)
        self.buttonDelay.grid(row=2, column=5)
        self.buttonQuit.grid(row=5, column=4)
        self.testReset.grid(row=5, column=3)
        
 
    def processIncoming(self):    
        while self.queue.qsize(  ):
            try:
                msg = self.queue.get(0).strip()
                print(msg[-1:]  + " " + msg[0])
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
        print("new cord " + cord)
        self.buttongroup[cord].configure(bg=self.color)
        self.pointTotal = add_points(self.point1C, self.pointTotal)
        print (self.pointTotal)
        self.label_pointTotal.config(text = "Point Total: " + str(self.pointTotal))
#        self.button1C.configure(state = DISABLED)
#        self.button1B.configure(state = NORMAL)
#        self.button2B.configure(state = NORMAL)
#        self.button2B.configure(state = NORMAL)
#        self.button3B.configure(state = DISABLED)
#        self.button3C.configure(state = DISABLED)
#        self.buttonAttack.configure(state = DISABLED)

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
    
    
