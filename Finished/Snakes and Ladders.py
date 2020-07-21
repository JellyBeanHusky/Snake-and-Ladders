#Name: Chandrasekara Wasala Mudiyanselage Kasun Piumal Chandrasekara
#Student ID: B1600409
#Class Code: BIT100

import random
import tkinter.simpledialog
from tkinter import *
from tkinter import PhotoImage

#Feedback text to show when click on the "Feedback" button
FEEDBACK = """
Enjoyed the game? It's feedback time,
☆☆☆☆☆

Please comment your experience with the game for improvements.
We appriciate your feedback ☺ Thank you! """

#Introduction text to show when click on the "Info" button
INTRO = """
★ ☆ ✮ ✯ ★ ☆ ✮ ✯ ★ ☆ ✮ ✯ ★ ☆ ✮ ✯ ★ ☆ ✮ ✯ ★ ☆ ✮ ✯ ★ ★ ☆ 

▁ ▂ ▃ ▄ Introduction ▄ ▃ ▂ ▁

This is one player Snakes and Ladders game.
Game board includes 50 squares with 3 snakes and 4 ladders.
There is an option calls "Roll Dice".
Player should Roll the dice for move the position.
If player met ladders can climb up positions faster.
Player who reach the 50th position will be declared as the winner.

♚ ♛ ♜ ♝ ♞ ♟♚ ♛ ♜ ♝ ♞ ♟♚ ♛ ♜ ♝ ♞ ♟♚ ♛ ♜ ♝ ♞ ♟♚ ♛ """

#define variables
dice=0
pos=0

#Function to roll the dice and move player 
def RollTheDice():
    #define globals for allow access to variables of a function and allow access to each other variables
    global dice,pos,window
    global n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,n31,n32,n33,n34,n35,n36,n37,n38,n39,n40,n41,n42,n43,n44,n45,n46,n47,n48,n49,n50

   #Roll the Dice 
    dice=random.randint(1,6)
    pos=pos+dice
    label_1.config(text="You Rolled " + str(dice))
    label_2.config(text="☛ Move forward to " +str(pos))
    #checks if user's location if greater then 50
    if pos > 50:
        pos = 50 - (pos-50)
        label_1.config(text="You Rolled " + str(dice))
        label_2.config(text="☚ Go back to " +str(pos))

    #Snakes positions
    if pos== 28:
        pos=13
        label_2.config(text="It's a snake ☹ Go back to 13")
        
    elif pos== 39:
        pos=34
        label_2.config(text="It's a snake ☹ Go back to 34")

    elif pos== 48:
        pos=44
        label_2.config(text="It's a snake ☹ Go back to 44")

    #Ladders positions
    if pos== 3:
        pos=8
        label_2.config(text="Wow! It's a ladder ☺ Move to 8")
        
    elif pos== 6:
        pos=26
        label_2.config(text="Wow! It's a ladder ☺ Move to 26")

    elif pos== 14:
        pos=22
        label_2.config(text="Wow! It's a ladder ☺ Move to 22")

    elif pos== 32:
        pos=49
        label_2.config(text="Wow! It's a ladder ☺ Move to 49")

    #Reset all blocks into default images
    n1.config(image=one)
    n2.config(image=two)
    n3.config(image=three)
    n4.config(image=four)
    n5.config(image=five)
    n6.config(image=six)
    n7.config(image=seven)
    n8.config(image=eight)
    n9.config(image=nine)
    n10.config(image=ten)
    n11.config(image=eleven)
    n12.config(image=twel)
    n13.config(image=thtn)
    n14.config(image=ftn)
    n15.config(image=fftn)
    n16.config(image=sxtn)
    n17.config(image=svtn)
    n18.config(image=etn)
    n19.config(image=nntn)
    n20.config(image=twty)
    n21.config(image=tw1)
    n22.config(image=tw2)
    n23.config(image=tw3)
    n24.config(image=tw4)
    n25.config(image=tw5)
    n26.config(image=tw6)
    n27.config(image=tw7)
    n28.config(image=tw8)
    n29.config(image=tw9)
    n30.config(image=trty)
    n31.config(image=tr1)
    n32.config(image=tr2)
    n33.config(image=tr3)
    n34.config(image=tr4)
    n35.config(image=tr5)
    n36.config(image=tr6)
    n37.config(image=tr7)
    n38.config(image=tr8)
    n39.config(image=tr9)
    n40.config(image=fty)
    n41.config(image=ft1)
    n42.config(image=ft2)
    n43.config(image=ft3)
    n44.config(image=ft4)
    n45.config(image=ft5)
    n46.config(image=ft6)
    n47.config(image=ft7)
    n48.config(image=ft8)
    n49.config(image=ft9)
    n50.config(image=ffty)

    #Move the player position and shows it black color
    if pos==1:
        n1.config(image=onei)
    if pos==2:
        n2.config(image=twoi)
    if pos==3:
        n3.config(image=threei)
    if pos==4:
        n4.config(image=fouri)
    if pos==5:
        n5.config(image=fivei)
    if pos==6:
        n6.config(image=sixi)
    if pos==7:
        n7.config(image=seveni)
    if pos==8:
        n8.config(image=eighti)
    if pos==9:
        n9.config(image=ninei)
    if pos==10:
        n10.config(image=teni)
    if pos==11:
        n11.config(image=eleveni)
    if pos==12:
        n12.config(image=tweli)
    if pos==13:
        n13.config(image=thtni)
    if pos==14:
        n14.config(image=ftni)
    if pos==15:
        n15.config(image=fftni)
    if pos==16:
        n16.config(image=sxtni)
    if pos==17:
        n17.config(image=svtni)
    if pos==18:
        n18.config(image=etni)
    if pos==19:
        n19.config(image=nntni)
    if pos==20:
        n20.config(image=twtyi)
    if pos==21:
        n21.config(image=tw1i)
    if pos==22:
        n22.config(image=tw2i)
    if pos==23:
        n23.config(image=tw3i)
    if pos==24:
        n24.config(image=tw4i)
    if pos==25:
        n25.config(image=tw5i)
    if pos==26:
        n26.config(image=tw6i)
    if pos==27:
        n27.config(image=tw7i)
    if pos==28:
        n28.config(image=tw8i)
    if pos==29:
        n29.config(image=tw9i)
    if pos==30:
        n30.config(image=trtyi)
    if pos==31:
        n31.config(image=tr1i)
    if pos==32:
        n32.config(image=tr2i)
    if pos==33:
        n33.config(image=tr3i)
    if pos==34:
        n34.config(image=tr4i)
    if pos==35:
        n35.config(image=tr5i)
    if pos==36:
        n36.config(image=tr6i)
    if pos==37:
        n37.config(image=tr7i)
    if pos==38:
        n38.config(image=tr8i)
    if pos==39:
        n39.config(image=tr9i)
    if pos==40:
        n40.config(image=ftyi)
    if pos==41:
        n41.config(image=ft1i)
    if pos==42:
        n42.config(image=ft2i)
    if pos==43:
        n43.config(image=ft3i)
    if pos==44:
        n44.config(image=ft4i)
    if pos==45:
        n45.config(image=ft5i)
    if pos==46:
        n46.config(image=ft6i)
    if pos==47:
        n47.config(image=ft7i)
    if pos==48:
        n48.config(image=ft8i)
    if pos==49:
        n49.config(image=ft9i)
    if pos==50:
        n50.config(image=fftyi)

    #Position to show when the player reach the top
    if pos==50:
        label_1.config(text="You Rolled "+ str(dice))
        label_2.config(text="Move to " +str(pos)+", Congratulations!! YOU WON! ♕")
        #After reach top position make it to 0 
        pos=0
#define the main window
window = Tk()
#define variables
entry = None

#Shows the feedback comment
def buttonPushed():
    global entry
    txt=entry.get()
    print ("Thank you! Your feedback is: " ,txt)
    #When click the "send feedback" button window close 
    FeedB.destroy()

#Text box for leave feedback
def textbox(parent):
    global entry
    entry= Entry(parent,width=60)
    entry.grid(row=2,pady=10)

#Additional popup window for introduction message
def NewWindow():
    NewWin = Toplevel()
    #Introduction text label, calibri 15 font and background "ffeec6" color code
    introduction = Label(NewWin, text=INTRO, font="calibri 15", bg="#ffeec6", height=15)
    introduction.grid()

#Additional popup window for feedback
def FeedbackWin():
    global FeedB, feed_btn
    FeedB = Toplevel()
    FeedB.config(bg="white")
    #Feedback text label, calibri 12 font and background white color
    feedbk = Label(FeedB, text=FEEDBACK, font="calibri 12",bg="white")
    #label position
    feedbk.grid(row=1,pady=5)
    
    #"Send feedback" button 
    feed_btn= Button(FeedB, bg="white", command=buttonPushed)
    #button replaced with an image
    feed_btn.config(image=submit,bd=0, relief=SOLID)
    #button position
    feed_btn.grid(row=3,pady=10)

    textbox(FeedB)
#Heading image
logo= PhotoImage(file="logo/logosnakesandladders1.png")
#Quit Game button image
img= PhotoImage(file="Buttons/quit.png")
#Roll Dice button image
img2= PhotoImage(file="Buttons/dice1.png")
#Information button image
infor= PhotoImage(file="Buttons/info.png")
#Feedback button image
feedback= PhotoImage(file="Buttons/feed2.png")
#Send Feedback button image
submit= PhotoImage(file="Buttons/sub.png")

#All block images on game board
one=PhotoImage(file="Game Board/1.png")
two=PhotoImage(file="Game Board/2.png")
three=PhotoImage(file="Game Board/3.png")
four=PhotoImage(file="Game Board/4.png")
five=PhotoImage(file="Game Board/5.png")
six=PhotoImage(file="Game Board/6.png")
seven=PhotoImage(file="Game Board/7.png")
eight=PhotoImage(file="Game Board/8.png")
nine=PhotoImage(file="Game Board/9.png")
ten=PhotoImage(file="Game Board/10.png")

eleven=PhotoImage(file="Game Board/11.png")
twel=PhotoImage(file="Game Board/12.png")
thtn=PhotoImage(file="Game Board/13.png")
ftn=PhotoImage(file="Game Board/14.png")
fftn=PhotoImage(file="Game Board/15.png")
sxtn=PhotoImage(file="Game Board/16.png")
svtn=PhotoImage(file="Game Board/17.png")
etn=PhotoImage(file="Game Board/18.png")
nntn=PhotoImage(file="Game Board/19.png")
twty=PhotoImage(file="Game Board/20.png")

tw1=PhotoImage(file="Game Board/21.png")
tw2=PhotoImage(file="Game Board/22.png")
tw3=PhotoImage(file="Game Board/23.png")
tw4=PhotoImage(file="Game Board/24.png")
tw5=PhotoImage(file="Game Board/25.png")
tw6=PhotoImage(file="Game Board/26.png")
tw7=PhotoImage(file="Game Board/27.png")
tw8=PhotoImage(file="Game Board/28.png")
tw9=PhotoImage(file="Game Board/29.png")
trty=PhotoImage(file="Game Board/30.png")

tr1=PhotoImage(file="Game Board/31.png")
tr2=PhotoImage(file="Game Board/32.png")
tr3=PhotoImage(file="Game Board/33.png")
tr4=PhotoImage(file="Game Board/34.png")
tr5=PhotoImage(file="Game Board/35.png")
tr6=PhotoImage(file="Game Board/36.png")
tr7=PhotoImage(file="Game Board/37.png")
tr8=PhotoImage(file="Game Board/38.png")
tr9=PhotoImage(file="Game Board/39.png")
fty=PhotoImage(file="Game Board/40.png")

ft1=PhotoImage(file="Game Board/41.png")
ft2=PhotoImage(file="Game Board/42.png")
ft3=PhotoImage(file="Game Board/43.png")
ft4=PhotoImage(file="Game Board/44.png")
ft5=PhotoImage(file="Game Board/45.png")
ft6=PhotoImage(file="Game Board/46.png")
ft7=PhotoImage(file="Game Board/47.png")
ft8=PhotoImage(file="Game Board/48.png")
ft9=PhotoImage(file="Game Board/49.png")
ffty=PhotoImage(file="Game Board/50.png")

#Image positions with "Player one" icon
onei=PhotoImage(file="Game Board/1 copy.png")
twoi=PhotoImage(file="Game Board/2 copy.png")
threei=PhotoImage(file="Game Board/3 copy.png")
fouri=PhotoImage(file="Game Board/4 copy.png")
fivei=PhotoImage(file="Game Board/5 copy.png")
sixi=PhotoImage(file="Game Board/6 copy.png")
seveni=PhotoImage(file="Game Board/7 copy.png")
eighti=PhotoImage(file="Game Board/8 copy.png")
ninei=PhotoImage(file="Game Board/9 copy.png")
teni=PhotoImage(file="Game Board/10 copy.png")

eleveni=PhotoImage(file="Game Board/11 copy.png")
tweli=PhotoImage(file="Game Board/12 copy.png")
thtni=PhotoImage(file="Game Board/13 copy.png")
ftni=PhotoImage(file="Game Board/14 copy.png")
fftni=PhotoImage(file="Game Board/15 copy.png")
sxtni=PhotoImage(file="Game Board/16 copy.png")
svtni=PhotoImage(file="Game Board/17 copy.png")
etni=PhotoImage(file="Game Board/18 copy.png")
nntni=PhotoImage(file="Game Board/19 copy.png")
twtyi=PhotoImage(file="Game Board/20 copy.png")

tw1i=PhotoImage(file="Game Board/21 copy.png")
tw2i=PhotoImage(file="Game Board/22 copy.png")
tw3i=PhotoImage(file="Game Board/23 copy.png")
tw4i=PhotoImage(file="Game Board/24 copy.png")
tw5i=PhotoImage(file="Game Board/25 copy.png")
tw6i=PhotoImage(file="Game Board/26 copy.png")
tw7i=PhotoImage(file="Game Board/27 copy.png")
tw8i=PhotoImage(file="Game Board/28 copy.png")
tw9i=PhotoImage(file="Game Board/29 copy.png")
trtyi=PhotoImage(file="Game Board/30 copy.png")

tr1i=PhotoImage(file="Game Board/31 copy.png")
tr2i=PhotoImage(file="Game Board/32 copy.png")
tr3i=PhotoImage(file="Game Board/33 copy.png")
tr4i=PhotoImage(file="Game Board/34 copy.png")
tr5i=PhotoImage(file="Game Board/35 copy.png")
tr6i=PhotoImage(file="Game Board/36 copy.png")
tr7i=PhotoImage(file="Game Board/37 copy.png")
tr8i=PhotoImage(file="Game Board/38 copy.png")
tr9i=PhotoImage(file="Game Board/39 copy.png")
ftyi=PhotoImage(file="Game Board/40 copy.png")

ft1i=PhotoImage(file="Game Board/41 copy.png")
ft2i=PhotoImage(file="Game Board/42 copy.png")
ft3i=PhotoImage(file="Game Board/43 copy.png")
ft4i=PhotoImage(file="Game Board/44 copy.png")
ft5i=PhotoImage(file="Game Board/45 copy.png")
ft6i=PhotoImage(file="Game Board/46 copy.png")
ft7i=PhotoImage(file="Game Board/47 copy.png")
ft8i=PhotoImage(file="Game Board/48 copy.png")
ft9i=PhotoImage(file="Game Board/49 copy.png")
fftyi=PhotoImage(file="Game Board/50 copy.png")

#Heading image position and label
w1=Label(window, image=logo,bg="white").grid(columnspan=10,row=0, column=0)

#define quit button
def exit():
    global window
    window.destroy()

#define the game interface
def GameWindow():
    #Define global
    global window,button1,button2,label_1,label_2,dice,pos,f,space, name
    global n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,n31,n32,n33,n34,n35,n36,n37,n38,n39,n40,n41,n42,n43,n44,n45,n46,n47,n48,n49,n50

    #Define the title
    window.title("Snake and Ladder")
    #Make the window white color
    window.config(bg="white")

    #for ask player name
    name= tkinter.simpledialog.askstring("Player 01", "Enter your name")
    #Introduction button
    info=Button(window,bg="white",command=NewWindow)
    #Button replaced with an image
    info.config(image=infor,bd=0, relief=SOLID)
    #button position
    info.grid(row=1, column=0,sticky=E, padx=5,pady=5)

    #Feedback button replaced with an image
    feedb=Button(window,bg="white")
    #Button replaced with an image
    feedb.config(image=feedback,bd=0, relief=SOLID,command=FeedbackWin)
    #Label position
    feedb.grid(row=1, column=0,sticky=W, padx=5,pady=3)    

    #Game board frame
    f=Frame(window,bd=1,relief=GROOVE,pady=10,padx=10,bg="#f6bf7d")
    f.grid()

    #Game board
    #Put all the blocks into "f" frame
    #Replace images as blocks
    n1=Label(f, image=one,bg="black")
    n2=Label(f,  image=two,bg="black")
    n3=Label(f, image=three,bg="black")
    n4=Label(f,  image=four,bg="black")
    n5=Label(f,  image=five,bg="black")
    n6=Label(f,  image=six,bg="black")
    n7=Label(f,  image=seven,bg="black")
    n8=Label(f,  image=eight,bg="black")
    n9=Label(f,  image=nine,bg="black")
    n10=Label(f, image=ten,bg="black")
    
    n11=Label(f,  image=eleven,bg="black")
    n12=Label(f,  image=twel,bg="black")
    n13=Label(f,  image=thtn,bg="black")
    n14=Label(f,  image=ftn,bg="black")
    n15=Label(f,  image=fftn,bg="black")
    n16=Label(f,  image=sxtn,bg="black")
    n17=Label(f,  image=svtn,bg="black")
    n18=Label(f,  image=etn,bg="black")
    n19=Label(f,  image=nntn,bg="black")
    n20=Label(f,  image=twty,bg="black")
    
    n21=Label(f,  image=tw1,bg="black")
    n22=Label(f,  image=tw2,bg="black")
    n23=Label(f,  image=tw3,bg="black")
    n24=Label(f,  image=tw4,bg="black")
    n25=Label(f,  image=tw5,bg="black")
    n26=Label(f,  image=tw6,bg="black")
    n27=Label(f,  image=tw7,bg="black")
    n28=Label(f,  image=tw8,bg="black")
    n29=Label(f,  image=tw9,bg="black")
    n30=Label(f,  image=trty,bg="black")
    
    n31=Label(f,  image=tr1,bg="black")
    n32=Label(f,  image=tr2,bg="black")
    n33=Label(f, image=tr3,bg="black")
    n34=Label(f,  image=tr4,bg="black")
    n35=Label(f,  image=tr5,bg="black")
    n36=Label(f,  image=tr6,bg="black")
    n37=Label(f,  image=tr7,bg="black")
    n38=Label(f,  image=tr8,bg="black")
    n39=Label(f,  image=tr9,bg="black")
    n40=Label(f, image=fty,bg="black")
    
    n41=Label(f, image=ft1,bg="black")
    n42=Label(f, image=ft2,bg="black")
    n43=Label(f, image=ft3,bg="black")
    n44=Label(f, image=ft4,bg="black")
    n45=Label(f, image=ft5,bg="black")
    n46=Label(f, image=ft6,bg="black")
    n47=Label(f, image=ft7,bg="black")
    n48=Label(f, image=ft8,bg="black")
    n49=Label(f, image=ft9,bg="black")
    n50=Label(f, image=ffty,bg="black")

    #Positions of each block of the game board
    n1.grid(row=10, column=0)
    n2.grid(row=10, column=1)
    n3.grid(row=10, column=2)
    n4.grid(row=10, column=3)
    n5.grid(row=10, column=4)
    n6.grid(row=10, column=5)
    n7.grid(row=10, column=6)
    n8.grid(row=10, column=7)
    n9.grid(row=10, column=8)
    n10.grid(row=10, column=9)
 
    n11.grid(row=9, column=9)
    n12.grid(row=9, column=8)
    n13.grid(row=9, column=7)
    n14.grid(row=9, column=6)
    n15.grid(row=9, column=5)
    n16.grid(row=9, column=4)
    n17.grid(row=9, column=3)
    n18.grid(row=9, column=2)
    n19.grid(row=9, column=1)
    n20.grid(row=9, column=0)

    n21.grid(row=8, column=0)
    n22.grid(row=8, column=1)
    n23.grid(row=8, column=2)
    n24.grid(row=8, column=3)
    n25.grid(row=8, column=4)
    n26.grid(row=8, column=5)
    n27.grid(row=8, column=6)
    n28.grid(row=8, column=7)
    n29.grid(row=8, column=8)
    n30.grid(row=8, column=9)

    n31.grid(row=7, column=9)
    n32.grid(row=7, column=8)
    n33.grid(row=7, column=7)
    n34.grid(row=7, column=6)
    n35.grid(row=7, column=5)
    n36.grid(row=7, column=4)
    n37.grid(row=7, column=3)
    n38.grid(row=7, column=2)
    n39.grid(row=7, column=1)
    n40.grid(row=7, column=0)

    n41.grid(row=6, column=0)
    n42.grid(row=6, column=1)
    n43.grid(row=6, column=2)
    n44.grid(row=6, column=3)
    n45.grid(row=6, column=4)
    n46.grid(row=6, column=5)
    n47.grid(row=6, column=6)
    n48.grid(row=6, column=7)
    n49.grid(row=6, column=8)
    n50.grid(row=6, column=9)
    
    #Label to show the number when dice is rolling
    label_1=Label(window,text="Roll Your Dice",font="calibri 20",bg="white",height=1)
    #Label position
    label_1.grid(columnspan=10,row=10, column=0)

    #Button for roll dice
    button1 = Button(window, command=RollTheDice,bg="white")
    #Replace image as a button
    button1.config(image=img2,bd=0, relief=SOLID)
    #Roll Dice button position
    button1.grid(columnspan=10,row=12, column=0)

    #Button for quit game
    button2= Button(window,command=exit)
    #Replace image as a button
    button2.config(image=img,bd=0, relief=SOLID)
    #Quit Game button position
    button2.grid(columnspan=10,row=13, column=0,padx=5)
    
    #Label to show movements of player and other information
    label_2=Label(window,text="Hi "+name+"," " Welcome to Snakes and Ladders" ,font="Calibri 15",fg="green",bg="white",height=2)
    #Label position
    label_2.grid(columnspan=10,row=11, column=0)

    #Empty space area
    space=Label(window,height=1,bg="white")
    #Label position
    space.grid(columnspan=10,row=14, column=0)
    
    window.mainloop()
GameWindow() 
