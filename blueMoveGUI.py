from tkinter import *

def blueMove():
    root = Tk() #begin tkinter gui
    
    defense='lightblue' #Define the color of defense team move
    height = 4
    width = 12
    
        
    #create a class of functions for each button
    class Moves:
        pointTotal = 0
        point1A = 70
        point1B = 80
        point1C = 90 
        point2A = 40 
        point2B = 50 
        point2C = 60 
        point3A = 10 
        point3B = 20 
        point3C = 30 
    
        def Color1A():
            button1A.configure(bg=defense)
            Moves.pointTotal = Moves.pointTotal + Moves.point1A
            print (Moves.pointTotal)
        def Color2A():
            button2A.configure(bg=defense)
            Moves.pointTotal = Moves.pointTotal + Moves.point2A
            print (Moves.pointTotal)
        def Color3A():
            button3A.configure(bg=defense)
            Moves.pointTotal = Moves.pointTotal + Moves.point3A
            print (Moves.pointTotal)
        def Color1B():
            button1B.configure(bg=defense)
            Moves.pointTotal = Moves.pointTotal + Moves.point1B
            print (Moves.pointTotal)
        def Color2B():
            button2B.configure(bg=defense)
            Moves.pointTotal = Moves.pointTotal + Moves.point2B
            print (Moves.pointTotal)
        def Color3B():
            button3B.configure(bg=defense)
            Moves.pointTotal = Moves.pointTotal + Moves.point3B
            print (Moves.pointTotal)
        def Color1C():
            button1C.configure(bg=defense)
            Moves.pointTotal = Moves.pointTotal + Moves.point1C
            print (Moves.pointTotal)
        def Color2C():
            button2C.configure(bg=defense)
            Moves.pointTotal = Moves.pointTotal + Moves.point2C
            print (Moves.pointTotal)
        def Color3C():
            button3C.configure(bg=defense)
            Moves.pointTotal = Moves.pointTotal + Moves.point3C
            print (Moves.pointTotal)
    
    
    #Assign text to labels
    label_1 = Label(root, text='1', height=height, width=width)
    label_2 = Label(root, text='2', height=height, width=width)
    label_3 = Label(root, text='3', height=height, width=width)
    label_A = Label(root, text='A', height=height, width=width)
    label_B = Label(root, text='B', height=height, width=width)
    label_C = Label(root, text='C', height=height, width=width)
    label_pointTotal = Label(root, text= "Point Total: %s" % Moves.pointTotal, height=height, width=width)
    
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
    
    root.mainloop() #Close the root function#

#Runs the defined function
blueMove()
