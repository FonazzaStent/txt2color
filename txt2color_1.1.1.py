import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
import os
import io
import pyperclip
import math
from tkinter import messagebox

img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAABuvAAAbrwFeGpEcAAAAB3RJTUUH5gQIDDglaXxNyAAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAASCSURBVFjDxZfLbxNXFMZ/c2fsscfxK7XzsPOAJC6BAHkRGpDaCnVFN62oFFVqpSB10Q3brtj2L0DKhmWXbLJHlboAKhVFbUOh0CaUQJqHkQMmTjy2x77ThcGxcWKPI7U90pU8d+6c+/k75zvnXsW2bZv/0TSnC20bHjxM8/ujDG63YGoiTDxmACClzW+LT3nyOIXfrzNx9ijhcNvhAMzPz3Pt2rW6hduls6wWTlaeFSRDnu9xK39jbQ1T3OzYe+cq4RlaAJGv8TE7O8vly5cbA7AsC02rJ2an2AtC7DGCIM8AhrZJ4VU7AlHlRKBYHai+jRofhUKhOQPFYhERDJLp6OCjkRFmL16kMxrll3u73Huw+zocNt9+dxfDnUN36xQMyRfffFDxIaXNx598jaqV+PHWT9yYu0nRtYtlWXUAxNsTOeDh6Chj587RNTLCQiqF7vUyORYhHHShKAqKotDl3SbS9gRd1wkeSeLWtcq7U2Mx+vq7UG0vpCNMjb1P6OEwxZSvOQOvdJ12j4fheByArWyWx8kkx+NxZj7rIZnMoao2t3+4hYIKqLjdJp9/+R6bG2l8bTrRjiAAv95eRpYkvYluVro3WLu7y27GxOf3HgwgJyUT0ShqVbyLUgLg0gQ9cQMpJR7dVfOdx+vmyEBHzVx2pxxzoQri41HS6ztYhWLjEHizWToDgcqzSwj6I5E66nRdrxn72ZHje4DaY0ECXTr+kK9xCL66dIkXuRx/JJO4VJXTPT0EvN465263e092irIvgNHpIdy6xsbTF/QNR3n39IeoqqgHYNs2K7srvCy8JKJH6Iv20h+NNiwg1f/6IACqKjh5ZoCTZwbK6rBKZP5KgrQxeiOoulYGcCd1h8XMYuXD6dA0k+2TDQFUMyCEaFrxSvki6/M/Y21ly+ACOvFLEwizZNZsDrDwaoGSXWrKQLMcqLbM8mZlc4DSdp7tR+to+/UiaUts2wbFGQMHhaDG51vZX2bFQhiawTHjWG3y+EfRROM+ZVlWZRSLxaYAfH0RFFEL1Hc0Ws6BC50XiG3HSOVTdHo6SfgTTR2aplmVbGrT9fo7bXR9Okp6cRWkTeBUHKM7XAagKiongida6uO5XK4lAADe7hDe7lC9DEtYrHKfHVKEiRNjGAXhGMB+3XNf29mB5eXy78FB8PvLAO5zk5esAJDiT7KkSXDecQiqE/JgGWTgxg14A3xhAWZmECaZyuZvbJ17SGRTBqpHU1te3tscIJ+HpSU0QX38VDQUFMchcHym22dO6BjEGKttIkw3BWCaZmXk8/nmAAYHwVXVQTUNBgfLOZDgPO30kiVNgCghultSgaMkDAZhZgaWlspsJBIQfi1DBYUIfUDfoWTopBQDEArB1NThjuWNVGAYxr9/L6ip4aVSDQOZTOa/BfC29HK5HPl83nkoGh3JnNjz58/r6sDa2tqhGGgJgJSS1dVVrl+/XiND0zSZm5vj2bNnSClbrQ/O7OrVq/bk5KStqmrDMT4+bl+5csWpW1txejtu9RLt5JDSUhI6ddiq/QMeSxpTDyo7FgAAAABJRU5ErkJggg=='

root= tk.Tk()
top= root
top.geometry("588x409+428+131")
top.resizable(0,0)
top.title("Text to Color")
favicon=tk.PhotoImage(data=img) 
root.wm_iconphoto(True, favicon)

#Textbox
textbox = Text(top)
textbox.place(relx=0.034, rely=0.049, relheight=0.888, relwidth=0.662)

scroll_1=Scrollbar (top)
scroll_1.place(relx=0.710, rely=0.030, relheight=0.930, anchor='n')
textbox.configure(yscrollcommand=scroll_1.set)
scroll_1.configure(command=textbox.yview)

#ColorDisplayFrame
ColorDisplayFrame= Frame(top)
ColorDisplayFrame.place(relx=0.748, rely=0.051, relheight=0.269, relwidth=0.23)
ColorDisplayFrame.configure(relief='groove')
ColorDisplayFrame.configure(borderwidth="2")
ColorDisplayFrame.configure(relief="groove")

#RedLabel
RedLabel=Label(top)
RedLabel.place(relx=0.748, rely=0.359, height=20, width=25)
RedLabel.configure(text='''Red''')

#RedField
RedField=Text(top)
RedField.place(relx=0.799, rely=0.367, relheight=0.061, relwidth=0.092)
RedField.configure(state='disabled')

#GreenLabel
GreenLabel=Label(top)
GreenLabel.place(relx=0.731, rely=0.438, height=20, width=35)
GreenLabel.configure(text='''Green''')

#GreenField
GreenField= Text(top)
GreenField.place(relx=0.799, rely=0.44, relheight=0.061, relwidth=0.092)
GreenField.configure(state='disabled')

#BlueLabel
BlueLabel=Label(top)
BlueLabel.place(relx=0.731, rely=0.513, height=22, width=34)
BlueLabel.configure(text='''Blue''')

#BlueField
BlueField=Text(top)
BlueField.place(relx=0.799, rely=0.513, relheight=0.061, relwidth=0.092)
BlueField.configure(state='disabled')

#HEXLabel
HEXLabel=Label(top)
HEXLabel.place(relx=0.711, rely=0.616, height=12, width=34)
HEXLabel.configure(text='''HEX''')

#HEXField
HEXField=Text(top)
HEXField.place(relx=0.779, rely=0.592, relheight=0.061, relwidth=0.112)
HEXField.configure(state='disabled')

#CopyRed
CopyRed=Button(top)
CopyRed.place (relx=0.901, rely=0.359, height=24, width=47)
CopyRed.configure(text='''Copy''')

#CopyGreen
CopyGreen=Button(top)
CopyGreen.place(relx=0.901, rely=0.438, height=24, width=47)
CopyGreen.configure(text='''Copy''')

#CopyBlue
CopyBlue=Button(top)
CopyBlue.place(relx=0.901, rely=0.513, height=24, width=47)
CopyBlue.configure(text='''Copy''')

#CopyHEX
CopyHEX=Button(top)
CopyHEX.place(relx=0.901, rely=0.592, height=24, width=47)
CopyHEX.configure(text='''Copy''')

#PasteMenu
def paste_text():
        textbox.event_generate(("<<Paste>>"))

menu = Menu(root, tearoff = 0)
menu.add_command(label="Paste", command=paste_text)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
textbox.bind("<Button-3>", context_menu)


#GenerateColor
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
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb
def GenerateColor():
    global blue
    blue=0
    global red
    red=0
    global green
    green=0
    global numbersum
    numbersum=0
    text=textbox.get(1.0,2000.0)
    textvalidate=0
    length=len(text)
    for letters in range (0,length):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            textvalidate=1
    if textvalidate==0:
        text="Hello"
    length=len(text)
    for letters in range (0,length):
        char=text[letters]
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
    redvalue=int(lightness*R/100)
    greenvalue=int(lightness*G/100)
    bluevalue=int(lightness*B/100)
    hexcolor=rgb_hack((redvalue,greenvalue,bluevalue))
    ColorDisplayFrame.configure(bg=hexcolor)
    RedField.configure(state='normal')
    RedField.delete(1.0,2000.0)
    RedField.insert(INSERT,redvalue)
    RedField.configure(state='disabled')
    GreenField.configure(state='normal')
    GreenField.delete(1.0,2000.0)
    GreenField.insert(INSERT,greenvalue)
    GreenField.configure(state='disabled')
    BlueField.configure(state='normal')
    BlueField.delete(1.0,2000.0)
    BlueField.insert(INSERT,bluevalue)
    BlueField.configure(state='disabled')
    HEXField.configure(state='normal')
    HEXField.delete(1.0,2000.0)
    HEXField.insert(INSERT,hexcolor)
    HEXField.configure(state='disabled')

#Generate color hotkey
def GenerateColor_hotkey(event):
    GenerateColor()

#Copy Red
def CopyRedfn(event):
    colorvalue=RedField.get(1.0,1.3)
    pyperclip.copy(colorvalue)

#Copy Green
def CopyGreenfn(event):
    colorvalue=GreenField.get(1.0,1.3)
    pyperclip.copy(colorvalue)

#Copy Blue
def CopyBluefn(event):
    colorvalue=BlueField.get(1.0,1.3)
    pyperclip.copy(colorvalue)

#Copy HEX
def CopyHEXfn(event):
    colorvalue=HEXField.get(1.0,1.7)
    pyperclip.copy(colorvalue)

#Paste From Button
def paste():
        textbox.event_generate(("<<Paste>>"))

#paste hotkey
def paste_hotkey(event):
    paste()

#Clear
def ClearTextBox():
    textbox.delete(1.0,2000.0)

def ClearTextBox_hotkey(event):
    ClearTextBox()

#Quit
def QuitApp():
    okcancel= messagebox.askokcancel("Quit?","Do you want to quit the app?",default="ok")
    if okcancel== True:
        top.destroy()

def Quit_hotkey (event):
    QuitApp()


menubar=tk.Menu(top, tearoff=0)
top.configure(menu=menubar)
sub_menu=tk.Menu(top, tearoff=0)
menubar.add_cascade(menu=sub_menu,compound="left", label="File")
sub_menu.add_command(compound="left", label="Paste", command=paste, accelerator="Alt+P")
sub_menu.add_command(compound="left",label="Clear", command=ClearTextBox, accelerator="Alt+C")
sub_menu.add_command(compound="left",label="Generate Color", command=GenerateColor,accelerator="Alt+G")
sub_menu.add_command(compound="left",label="Quit", command=QuitApp, accelerator="Alt+Q")
top.bind_all("<Alt-p>",paste_hotkey)
top.bind_all("<Alt-c>",ClearTextBox_hotkey)
top.bind_all("<Alt-g>",GenerateColor_hotkey)
top.bind_all("<Alt-q>",Quit_hotkey)
menubar.bind_all("<Alt-f>",menubar.invoke(1))

CopyRed.bind("<Button-1>",CopyRedfn)
CopyGreen.bind("<Button-1>",CopyGreenfn)
CopyBlue.bind("<Button-1>",CopyBluefn)
CopyHEX.bind("<Button-1>",CopyHEXfn)

textbox.focus_set()


root.mainloop()
