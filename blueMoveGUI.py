# Programmer: Elliott Fix
# Temple University, College of Engineering
# Start Date: December, 2016
# Version: 0.1
# Code inspired by Shakeel Osmani
#        https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/
# Description: A basic CLient-Server program that features two client GUIs for
#              two players to compete in a game setting that models the attack
#              and defense of Internet security.


from tkinter import *
from tkinter import messagebox

def blueMove():
    root = Tk() #begin tkinter gui
    
    
    color = 'lightblue' #Define the color of team move
    height = 4
    width = 12
    
    def quit():
        root.destroy()
    
    #create a class of functions for each button
    class Moves:
        pointTotal = 400
        pingCost = 30
        delayCost = 10
        point1A = 70
        point1B = 40
        point1C = 10 
        point2A = 80 
        point2B = 50 
        point2C = 20 
        point3A = 90 
        point3B = 60 
        point3C = 30 
    
        def Color1A():
            button1A.configure(bg=color)
            
            if Moves.pointTotal < Moves.point1A:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point1A
                print (Moves.pointTotal)
            
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def Color2A():
            button2A.configure(bg=color)

            if Moves.pointTotal < Moves.point2A:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point2A
                print (Moves.pointTotal)
            
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def Color3A():
            button3A.configure(bg=color)
            
            if Moves.pointTotal < Moves.point3A:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point3A
                print (Moves.pointTotal)
            
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def Color1B():
            button1B.configure(bg=color)
            
            if Moves.pointTotal < Moves.point1B:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point1B
                print (Moves.pointTotal)
            
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def Color2B():
            button2B.configure(bg=color)
            
            if Moves.pointTotal < Moves.point2B:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point2B
                print (Moves.pointTotal)
            
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def Color3B():
            button3B.configure(bg=color)
            
            if Moves.pointTotal < Moves.point3B:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point3B
                print (Moves.pointTotal)
            
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def Color1C():
            button1C.configure(bg=color)
            
            if Moves.pointTotal < Moves.point1C:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point1C
                print (Moves.pointTotal)
            
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def Color2C():
            button2C.configure(bg=color)
            
            if Moves.pointTotal < Moves.point2C:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point2C
                print (Moves.pointTotal)
            
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def Color3C():
            button3C.configure(bg=color)
            
            if Moves.pointTotal < Moves.point3C:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point3C
                print (Moves.pointTotal)
            
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def DelayMove():
            Moves.pointTotal = Moves.pointTotal - Moves.delayCost
            
            if Moves.pointTotal < Moves.delayCost:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - Moves.point3C
                print ("Move Delayed")
                
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
            
        def testReset():
            Moves.pointTotal = 400
            button1A.configure(state = NORMAL, bg='gray95')
            button1B.configure(state = NORMAL, bg='gray95')
            button1C.configure(state = NORMAL, bg='gray95')
            button2A.configure(state = NORMAL, bg='gray95')
            button2B.configure(state = NORMAL, bg='gray95')
            button2C.configure(state = NORMAL, bg='gray95')
            button3A.configure(state = NORMAL, bg='gray95')
            button3B.configure(state = NORMAL, bg='gray95')
            button3C.configure(state = NORMAL, bg='gray95')
            
        def pingRed():
            #Request red's location from server
            
            if Moves.pointTotal < pingCost:
                var = messagebox.showinfo("Invalid Move", "You do not have enough resources!")
            else:
                Moves.pointTotal = Moves.pointTotal - pingCost   
                         
            print (Moves.pointTotal)
            label_pointTotal.config(text = "Point Total: " + str(Moves.pointTotal))
    
    #Assign text to labels
    label_1 = Label(root, text='1', height=height, width=width)
    label_2 = Label(root, text='2', height=height, width=width)
    label_3 = Label(root, text='3', height=height, width=width)
    label_A = Label(root, text='A', height=height, width=width)
    label_B = Label(root, text='B', height=height, width=width)
    label_C = Label(root, text='C', height=height, width=width)
    label_pointTotal = Label(root, text = "Point Total: " + str(Moves.pointTotal), height=height, width=width)
    
    #Define buttons
    button1A = Button(root, text = Moves.point1A, command = Moves.Color1A, height=height, width=width)
    button1B = Button(root, text = Moves.point1B, command = Moves.Color1B, height=height, width=width)
    button1C = Button(root, text = Moves.point1C, command = Moves.Color1C, height=height, width=width)
    button2A = Button(root, text = Moves.point2A, command = Moves.Color2A, height=height, width=width)
    button2B = Button(root, text = Moves.point2B, command = Moves.Color2B, height=height, width=width)
    button2C = Button(root, text = Moves.point2C, command = Moves.Color2C, height=height, width=width)
    button3A = Button(root, text = Moves.point3A, command = Moves.Color3A, height=height, width=width)
    button3B = Button(root, text = Moves.point3B, command = Moves.Color3B, height=height, width=width)
    button3C = Button(root, text = Moves.point3C, command = Moves.Color3C, height=height, width=width)
    buttonPing = Button(root, text = 'Ping Red\nPosition', height=height, width=width, state = NORMAL)
    buttonDelay = Button(root, text = "Delay\nMove", command = Moves.DelayMove, height=height, width=width)
    buttonQuit = Button(root, text = "Quit", command = quit, height=height, width=width)
    testReset = Button(root, text = "Test\nReset", command = Moves.testReset, height=height, width=width)
    
    
    #Align labels and buttons in grid
    label_1.grid(row=0, column=1)
    label_2.grid(row=0, column=2)
    label_3.grid(row=0, column=3)
    label_A.grid(row=1, column=0)
    label_B.grid(row=2, column=0)
    label_C.grid(row=3, column=0)
    label_pointTotal.grid(columnspan=4)
    button1A.grid(row=1, column=1)
    button1B.grid(row=2, column=1)
    button1C.grid(row=3, column=1)
    button2A.grid(row=1, column=2)
    button2B.grid(row=2, column=2)
    button2C.grid(row=3, column=2)
    button3A.grid(row=1, column=3)
    button3B.grid(row=2, column=3)
    button3C.grid(row=3, column=3)
    buttonPing.grid(row=1, column=5)
    buttonDelay.grid(row=2, column=5)
    buttonQuit.grid(row=5, column=4)
    testReset.grid(row=5, column=3)
    
    
    root.mainloop() #Displays the window

#Runs the defined function
blueMove()
