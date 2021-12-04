import os
import math
from tkinter import *

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

def textinput():
    text= str(input("Input text (letters only, max 50 characters, 0 to quit): "))
    if len(text)==0:
        textinput()
    if text=="0":
        quit()
    return text

c=9.84
rc=28.44
bc=23.27
gc=36.57

blue=0
red=0
green=0
lettern=1
numbersum=0

def sine(value, letternumber):
    global blue
    blue=blue+value
    global lettern
    lettern=letternumber
    global numbersum
    numbersum=numbersum+lettern

def triangle (value, letternumber):
    global red
    red=red+value
    global lettern
    lettern=letternumber
    global numbersum
    numbersum=numbersum+lettern    

def square (value, letternumber):
    global green
    green=green+value
    global lettern
    lettern=letternumber
    global numbersum
    numbersum=numbersum+lettern

def end():
    text.close

def main():
    global blue
    blue=0
    global red
    red=0
    global green
    green=0
    global numbersum
    numbersum=0
    textinput
    text=textinput()
    length=len(text)
    if length>50:
        text=text[0:50]
        length=len(text)
    for letters in range (0,length):
        char=text[letters]
        if char=='':
            end
        else:
            asciicode=ord(char)
            if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
                if char=="A" or char=="a":
                    triangle(int(1*rc), 1)
                if char=="B" or char=="b":
                    sine (int(1*bc), 2)
                if char=="C" or char=="c":
                    sine(int(2*bc), 3)
                if char=="D" or char=="d":
                    sine(int(3*bc),4)
                if char=="E" or char=="e":
                    square(int(1*gc),5)
                if char=="F" or char=="f":
                    square(int(2*gc),6)
                if char=="G" or char=="g":
                    sine(int(4*bc),7)
                if char=="H" or char=="h":
                    square(int(3*gc),8)
                if char=="i" or char=="I":
                    square(int(4*gc),9)
                if char=="J" or char=="j":
                    sine(int(5*bc),10)
                if char=="K" or char=="k":
                    triangle(int(2*rc),11)
                if char=="L" or char=="l":
                    square(int(5*gc),12)
                if char=="M" or char=="m":
                    triangle(int(3*rc),13)
                if char=="N" or char=="n":
                    triangle(int(4*rc),14)
                if char=="O" or char=="o":
                    sine(int(6*bc),15)
                if char=="P" or char=="p":
                    sine(int(7*bc),16)
                if char=="Q" or char=="q":
                    sine(int(8*bc),17)
                if char=="R" or char=="r":
                    sine(int(9*bc),18)
                if char=="S" or char=="s":
                    sine(int(10*bc),19)
                if char=="T" or char=="t":
                    square(int(5*gc),20)
                if char=="U" or char=="u":
                    sine(int(11*bc),21)
                if char=="V" or char=="v":
                    triangle(int(5*rc),22)
                if char=="W" or char=="w":
                    triangle(int(6*rc),23)
                if char=="X" or char=="x":
                    triangle(int(7*rc),24)
                if char=="Y" or char=="y":
                    triangle(int(8*rc),25)
                if char=="Z" or char=="z":
                    triangle(int(9*rc),26)
    blue=int(blue/length)
    red=int(red/length)
    green=int(green/length)
    RGB=[red,green,blue]
    maxvalue=max(RGB)
    R=int(255/maxvalue*red)
    G=int(255/maxvalue*green)
    B=int(255/maxvalue*blue)
    maxlightness=length*26
    lightness=int(100*numbersum/maxlightness)
    Rl=int(lightness*R/100)
    Gl=int(lightness*G/100)
    Bl=int(lightness*B/100)
    hexcolor=rgb_hack((Rl,Gl,Bl))
    ws=Tk()
    ws.title("Resulting Color")
    ws.geometry('400x300')
    ws.config(bg=hexcolor)
    RGBstring=("R: " + str(Rl) + " G: " + str(Gl) + " B: " + str(Bl)+ "\n Hex: "+str(hexcolor))
    text_box = Text(
        ws,
        height=2,
        width=25
    )
    text_box.pack(expand=True)
    text_box.insert('end', RGBstring)
    text_box.config(state='disabled')

    ws.mainloop()

loop=1
while (loop==1):
    main()
end
    
    
