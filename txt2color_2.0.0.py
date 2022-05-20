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

#init
def init():
    global c
    global rc
    global bc
    global gc
    global blue
    global red
    global green
    global lettern
    global numbersum
    global redsum
    global greensum
    global bluesum
    global redlength
    global greenlength
    global bluelength
    c=9.84
    rc=28.44
    bc=23.27
    gc=42.5
    blue=0
    red=0
    green=0
    lettern=1
    numbersum=0
    redsum=0
    greensum=0
    bluesum=0
    redlength=0
    greenlength=0
    bluelength=0  

#Create app window
def create_app_window():
    global top
    global root
    img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAABuvAAAbrwFeGpEcAAAAB3RJTUUH5gQIDDglaXxNyAAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAASCSURBVFjDxZfLbxNXFMZ/c2fsscfxK7XzsPOAJC6BAHkRGpDaCnVFN62oFFVqpSB10Q3brtj2L0DKhmWXbLJHlboAKhVFbUOh0CaUQJqHkQMmTjy2x77ThcGxcWKPI7U90pU8d+6c+/k75zvnXsW2bZv/0TSnC20bHjxM8/ujDG63YGoiTDxmACClzW+LT3nyOIXfrzNx9ijhcNvhAMzPz3Pt2rW6hduls6wWTlaeFSRDnu9xK39jbQ1T3OzYe+cq4RlaAJGv8TE7O8vly5cbA7AsC02rJ2an2AtC7DGCIM8AhrZJ4VU7AlHlRKBYHai+jRofhUKhOQPFYhERDJLp6OCjkRFmL16kMxrll3u73Huw+zocNt9+dxfDnUN36xQMyRfffFDxIaXNx598jaqV+PHWT9yYu0nRtYtlWXUAxNsTOeDh6Chj587RNTLCQiqF7vUyORYhHHShKAqKotDl3SbS9gRd1wkeSeLWtcq7U2Mx+vq7UG0vpCNMjb1P6OEwxZSvOQOvdJ12j4fheByArWyWx8kkx+NxZj7rIZnMoao2t3+4hYIKqLjdJp9/+R6bG2l8bTrRjiAAv95eRpYkvYluVro3WLu7y27GxOf3HgwgJyUT0ShqVbyLUgLg0gQ9cQMpJR7dVfOdx+vmyEBHzVx2pxxzoQri41HS6ztYhWLjEHizWToDgcqzSwj6I5E66nRdrxn72ZHje4DaY0ECXTr+kK9xCL66dIkXuRx/JJO4VJXTPT0EvN465263e092irIvgNHpIdy6xsbTF/QNR3n39IeoqqgHYNs2K7srvCy8JKJH6Iv20h+NNiwg1f/6IACqKjh5ZoCTZwbK6rBKZP5KgrQxeiOoulYGcCd1h8XMYuXD6dA0k+2TDQFUMyCEaFrxSvki6/M/Y21ly+ACOvFLEwizZNZsDrDwaoGSXWrKQLMcqLbM8mZlc4DSdp7tR+to+/UiaUts2wbFGQMHhaDG51vZX2bFQhiawTHjWG3y+EfRROM+ZVlWZRSLxaYAfH0RFFEL1Hc0Ws6BC50XiG3HSOVTdHo6SfgTTR2aplmVbGrT9fo7bXR9Okp6cRWkTeBUHKM7XAagKiongida6uO5XK4lAADe7hDe7lC9DEtYrHKfHVKEiRNjGAXhGMB+3XNf29mB5eXy78FB8PvLAO5zk5esAJDiT7KkSXDecQiqE/JgGWTgxg14A3xhAWZmECaZyuZvbJ17SGRTBqpHU1te3tscIJ+HpSU0QX38VDQUFMchcHym22dO6BjEGKttIkw3BWCaZmXk8/nmAAYHwVXVQTUNBgfLOZDgPO30kiVNgCghultSgaMkDAZhZgaWlspsJBIQfi1DBYUIfUDfoWTopBQDEArB1NThjuWNVGAYxr9/L6ip4aVSDQOZTOa/BfC29HK5HPl83nkoGh3JnNjz58/r6sDa2tqhGGgJgJSS1dVVrl+/XiND0zSZm5vj2bNnSClbrQ/O7OrVq/bk5KStqmrDMT4+bl+5csWpW1txejtu9RLt5JDSUhI6ddiq/QMeSxpTDyo7FgAAAABJRU5ErkJggg=='
    root= tk.Tk()
    top= root
    #top.geometry("588x409+428+131")
    top.geometry("730x520")
    top.resizable(0,0)
    top.title("Text to Color")
    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)

#Textbox
def create_textbox():
    global textbox
    textbox = Text(top)
    textbox.place(x=20, y=20, height=470, width=400)
    scroll_1=Scrollbar (top)
    scroll_1.place(x=421, y=20, height=470, anchor='n')
    textbox.configure(yscrollcommand=scroll_1.set)
    scroll_1.configure(command=textbox.yview)
    textbox.focus_set()
    textbox.bind("<Button-3>", context_menu)



#ColorDisplayFrame
def create_color_display_frame():
    global ColorDisplayFrame
    ColorDisplayFrame= Frame(top)
    ColorDisplayFrame.place(x=435, y=20, height=150, width=100)
    ColorDisplayFrame.configure(relief='groove')
    ColorDisplayFrame.configure(borderwidth="2")
    ColorDisplayFrame.configure(relief="groove")

    global ColorDisplayFrame2
    ColorDisplayFrame2= Frame(top)
    ColorDisplayFrame2.place(x=435, y=180, height=150, width=100)
    ColorDisplayFrame2.configure(relief='groove')
    ColorDisplayFrame2.configure(borderwidth="2")
    ColorDisplayFrame2.configure(relief="groove")

    global ColorDisplayFrame3
    ColorDisplayFrame3= Frame(top)
    ColorDisplayFrame3.place(x=435, y=340, height=150, width=100)
    ColorDisplayFrame3.configure(relief='groove')
    ColorDisplayFrame3.configure(borderwidth="2")
    ColorDisplayFrame3.configure(relief="groove")



#CreateLabels
def create_labels_buttons():

#algorithm 1 (simple)
    
    #RedLabel
    global RedLabel
    RedLabel=Label(top)
    RedLabel.place(x=545, y=25, height=20, width=25)
    RedLabel.configure(text='''Red''')

    #RedField
    global RedField
    RedField=Text(top)
    RedField.place(x=590, y=20, height=30, width=70)
    RedField.configure(state='disabled')
    
    #CopyRed
    global CopyRed
    CopyRed=Button(top)
    CopyRed.place (x=670, y=23, height=24, width=47)
    CopyRed.configure(text='''Copy''')

    #GreenLabel
    global GreenLabel
    GreenLabel=Label(top)
    GreenLabel.place(x=545, y=65, height=20, width=30)
    GreenLabel.configure(text='''Green''')

    #GreenField
    global GreenField
    GreenField= Text(top)
    GreenField.place(x=590, y=60, height=30, width=70)
    GreenField.configure(state='disabled')
    
    #CopyGreen
    global CopyGreen
    CopyGreen=Button(top)
    CopyGreen.place(x=670, y=63, height=24, width=47)
    CopyGreen.configure(text='''Copy''')

    #BlueLabel
    global BlueLabel
    BlueLabel=Label(top)
    BlueLabel.place(x=545, y=105, height=22, width=34)
    BlueLabel.configure(text='''Blue''')

    #BlueField
    global BlueField
    BlueField=Text(top)
    BlueField.place(x=590, y=100, height=30, width=70)
    BlueField.configure(state='disabled')
    
    #CopyBlue
    global CopyBlue
    CopyBlue=Button(top)
    CopyBlue.place(x=670, y=103, height=24, width=47)
    CopyBlue.configure(text='''Copy''')

    #HEXLabel
    global HEXLabel
    HEXLabel=Label(top)
    HEXLabel.place(x=545, y=150, height=12, width=34)
    HEXLabel.configure(text='''HEX''')

    #HEXField
    global HEXField
    HEXField=Text(top)
    HEXField.place(x=590, y=140, height=30, width=70)
    HEXField.configure(state='disabled')

    #CopyHEX
    global CopyHEX
    CopyHEX=Button(top)
    CopyHEX.place(x=670, y=143, height=24, width=47)
    CopyHEX.configure(text='''Copy''')

#algorithm 2 (pop)

    #RedLabel
    global RedLabel2
    RedLabel2=Label(top)
    RedLabel2.place(x=545, y=185, height=20, width=25)
    RedLabel2.configure(text='''Red''')

    #RedField
    global RedField2
    RedField2=Text(top)
    RedField2.place(x=590, y=180, height=30, width=70)
    RedField2.configure(state='disabled')
    
    #CopyRed
    global CopyRed2
    CopyRed2=Button(top)
    CopyRed2.place (x=670, y=183, height=24, width=47)
    CopyRed2.configure(text='''Copy''')

    #GreenLabel
    global GreenLabel2
    GreenLabel2=Label(top)
    GreenLabel2.place(x=545, y=225, height=20, width=30)
    GreenLabel2.configure(text='''Green''')

    #GreenField
    global GreenField2
    GreenField2= Text(top)
    GreenField2.place(x=590, y=220, height=30, width=70)
    GreenField2.configure(state='disabled')
    
    #CopyGreen
    global CopyGreen2
    CopyGreen2=Button(top)
    CopyGreen2.place(x=670, y=223, height=24, width=47)
    CopyGreen2.configure(text='''Copy''')

    #BlueLabel
    global BlueLabel2
    BlueLabel2=Label(top)
    BlueLabel2.place(x=545, y=265, height=22, width=34)
    BlueLabel2.configure(text='''Blue''')

    #BlueField
    global BlueField2
    BlueField2=Text(top)
    BlueField2.place(x=590, y=265, height=30, width=70)
    BlueField2.configure(state='disabled')
    
    #CopyBlue
    global CopyBlue2
    CopyBlue2=Button(top)
    CopyBlue2.place(x=670, y=263, height=24, width=47)
    CopyBlue2.configure(text='''Copy''')

    #HEXLabel
    global HEXLabel2
    HEXLabel2=Label(top)
    HEXLabel2.place(x=545, y=310, height=12, width=34)
    HEXLabel2.configure(text='''HEX''')

    #HEXField
    global HEXField2
    HEXField2=Text(top)
    HEXField2.place(x=590, y=300, height=30, width=70)
    HEXField2.configure(state='disabled')

    #CopyHEX
    global CopyHEX2
    CopyHEX2=Button(top)
    CopyHEX2.place(x=670, y=303, height=24, width=47)
    CopyHEX2.configure(text='''Copy''')

#algorithm 3
    
    #RedLabel
    global RedLabel3
    RedLabel3=Label(top)
    RedLabel3.place(x=545, y=345, height=20, width=25)
    RedLabel3.configure(text='''Red''')

    #RedField
    global RedField3
    RedField3=Text(top)
    RedField3.place(x=590, y=340, height=30, width=70)
    RedField3.configure(state='disabled')
    
    #CopyRed
    global CopyRed3
    CopyRed3=Button(top)
    CopyRed3.place (x=670, y=343, height=24, width=47)
    CopyRed3.configure(text='''Copy''')

    #GreenLabel
    global GreenLabel3
    GreenLabel3=Label(top)
    GreenLabel3.place(x=545, y=385, height=20, width=30)
    GreenLabel3.configure(text='''Green''')

    #GreenField
    global GreenField3
    GreenField3= Text(top)
    GreenField3.place(x=590, y=380, height=30, width=70)
    GreenField3.configure(state='disabled')
    
    #CopyGreen
    global CopyGreen3
    CopyGreen3=Button(top)
    CopyGreen3.place(x=670, y=383, height=24, width=47)
    CopyGreen3.configure(text='''Copy''')

    #BlueLabel
    global BlueLabel3
    BlueLabel3=Label(top)
    BlueLabel3.place(x=545, y=425, height=22, width=34)
    BlueLabel3.configure(text='''Blue''')

    #BlueField
    global BlueField3
    BlueField3=Text(top)
    BlueField3.place(x=590, y=425, height=30, width=70)
    BlueField3.configure(state='disabled')
    
    #CopyBlue
    global CopyBlue3
    CopyBlue3=Button(top)
    CopyBlue3.place(x=670, y=423, height=24, width=47)
    CopyBlue3.configure(text='''Copy''')

    #HEXLabel
    global HEXLabel3
    HEXLabel3=Label(top)
    HEXLabel3.place(x=545, y=470, height=12, width=34)
    HEXLabel3.configure(text='''HEX''')

    #HEXField
    global HEXField3
    HEXField3=Text(top)
    HEXField3.place(x=590, y=460, height=30, width=70)
    HEXField3.configure(state='disabled')

    #CopyHEX
    global CopyHEX3
    CopyHEX3=Button(top)
    CopyHEX3.place(x=670, y=463, height=24, width=47)
    CopyHEX3.configure(text='''Copy''')    

#Create menu
def create_menu():
    global menubar
    global sub_menu
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left", label="Paste", command=paste, accelerator="Alt+P")
    sub_menu.add_command(compound="left",label="Clear", command=ClearTextBox, accelerator="Alt+C")
    sub_menu.add_command(compound="left",label="Generate Color", command=GenerateColor,accelerator="Alt+G")
    sub_menu.add_command(compound="left",label="Copy HEX value 1", command=CopyHEXfn,accelerator="Alt+H")
    sub_menu.add_command(compound="left",label="Copy HEX value 2", command=CopyHEXfn2,accelerator="Alt+J")
    sub_menu.add_command(compound="left",label="Copy HEX value 3", command=CopyHEXfn3,accelerator="Alt+K")
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp, accelerator="Alt+Q")
    top.bind_all("<Alt-p>",paste_hotkey)
    top.bind_all("<Alt-c>",ClearTextBox_hotkey)
    top.bind_all("<Alt-g>",GenerateColor_hotkey)
    top.bind_all("<Alt-q>",Quit_hotkey)
    top.bind_all("<Alt-h>",CopyHEXfn_hotkey)
    top.bind_all("<Alt-j>",CopyHEXfn2_hotkey)
    top.bind_all("<Alt-k>",CopyHEXfn3_hotkey)
    menubar.bind_all("<Alt-f>",menubar.invoke(1))

    CopyRed.bind("<Button-1>",CopyRedfn)
    CopyGreen.bind("<Button-1>",CopyGreenfn)
    CopyBlue.bind("<Button-1>",CopyBluefn)
    CopyHEX.bind("<Button-1>",CopyHEXfn_hotkey)

    CopyRed2.bind("<Button-1>",CopyRedfn2)
    CopyGreen2.bind("<Button-1>",CopyGreenfn2)
    CopyBlue2.bind("<Button-1>",CopyBluefn2)
    CopyHEX2.bind("<Button-1>",CopyHEXfn2_hotkey)

    CopyRed3.bind("<Button-1>",CopyRedfn3)
    CopyGreen3.bind("<Button-1>",CopyGreenfn3)
    CopyBlue3.bind("<Button-1>",CopyBluefn3)
    CopyHEX3.bind("<Button-1>",CopyHEXfn3_hotkey)

#PasteMenu
def paste_text():
        textbox.event_generate(("<<Paste>>"))



def context_menu(event):
    menu = Menu(root, tearoff = 0)
    menu.add_command(label="Paste", command=paste_text)
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()



#GenerateColor

def sine(value, letternumber):
    global blue
    blue=blue+value
    global bluelength
    bluelength=bluelength+1
    global bluesum
    bluesum=bluesum+letternumber

def triangle (value, letternumber):
    global red
    red=red+value
    global redlength
    redlength=redlength+1
    global redsum
    redsum=redsum+letternumber

def square (value, letternumber):
    global green
    green=green+value
    global greenlength
    greenlength= greenlength+1
    global greensum
    greensum=greensum+letternumber

def sine2(value, letternumber):
    global blue
    blue=blue+value
    global lettern
    lettern=letternumber
    global numbersum
    numbersum=numbersum+lettern

def triangle2 (value, letternumber):
    global red
    red=red+value
    global lettern
    lettern=letternumber
    global numbersum
    numbersum=numbersum+lettern    

def square2 (value, letternumber):
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
    global redsum
    global redlength
    global greensum
    global greenlength
    global bluesum
    global bluelength
    numbersum=0
    text=textbox.get(1.0,END)
    textvalidate=0
    length=len(text)-1
    for letters in range (0,length):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            textvalidate=1
    if textvalidate==0:
        text="Hello"
    length=len(text)-1
    for letters in range (0,length):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            if char=="A" or char=="a":
                triangle(int(1*rc), 1)
            if char=="B" or char=="b":
                sine (int(1*bc), 1)
            if char=="C" or char=="c":
                sine(int(2*bc), 2)
            if char=="D" or char=="d":
                sine(int(3*bc),3)
            if char=="E" or char=="e":
                square(int(1*gc),1)
            if char=="F" or char=="f":
                square(int(2*gc),2)
            if char=="G" or char=="g":
                sine(int(4*bc),4)
            if char=="H" or char=="h":
                square(int(3*gc),3)
            if char=="i" or char=="I":
                square(int(4*gc),4)
            if char=="J" or char=="j":
                sine(int(5*bc),5)
            if char=="K" or char=="k":
                triangle(int(2*rc),2)
            if char=="L" or char=="l":
                square(int(5*gc),5)
            if char=="M" or char=="m":
                triangle(int(3*rc),3)
            if char=="N" or char=="n":
                triangle(int(4*rc),4)
            if char=="O" or char=="o":
                sine(int(6*bc),6)
            if char=="P" or char=="p":
                sine(int(7*bc),7)
            if char=="Q" or char=="q":
                sine(int(8*bc),8)
            if char=="R" or char=="r":
                sine(int(9*bc),9)
            if char=="S" or char=="s":
                sine(int(10*bc),10)
            if char=="T" or char=="t":
                square(int(6*gc),6)
            if char=="U" or char=="u":
                sine(int(11*bc),11)
            if char=="V" or char=="v":
                triangle(int(5*rc),5)
            if char=="W" or char=="w":
                triangle(int(6*rc),6)
            if char=="X" or char=="x":
                triangle(int(7*rc),7)
            if char=="Y" or char=="y":
                triangle(int(8*rc),8)
            if char=="Z" or char=="z":
                triangle(int(9*rc),9)
    if bluelength>0:
        blue=int(blue/bluelength)
        bluevalue=int(blue*bluelength)
    else:
        blue=0
        bluevalue=0
    if redlength>0:
        red=int(red/redlength)
        redvalue=int(red*redlength)
    else:
        red=0
        redvalue=0
    if greenlength>0:
        green=int(green/greenlength)
        greenvalue=int(green*greenlength)
    else:
        green=0
        greenvalue=0
    RGB=[redvalue,greenvalue,bluevalue]
    RGB2=[red,green,blue]
    maxvalue=max(RGB)
    maxvalue2=max(RGB2)
    R=int(maxvalue2/maxvalue*redvalue)
    G=int(maxvalue2/maxvalue*greenvalue)
    B=int(maxvalue2/maxvalue*bluevalue)
    hexcolor=rgb_hack((R,G,B))
    ColorDisplayFrame.configure(bg=hexcolor)
    RedField.configure(state='normal')
    RedField.delete(1.0,2000.0)
    RedField.insert(INSERT,R)
    RedField.configure(state='disabled')
    GreenField.configure(state='normal')
    GreenField.delete(1.0,2000.0)
    GreenField.insert(INSERT,G)
    GreenField.configure(state='disabled')
    BlueField.configure(state='normal')
    BlueField.delete(1.0,2000.0)
    BlueField.insert(INSERT,B)
    BlueField.configure(state='disabled')
    HEXField.configure(state='normal')
    HEXField.delete(1.0,2000.0)
    HEXField.insert(INSERT,hexcolor)
    HEXField.configure(state='disabled')


#algorithm 2
    blue=0
    red=0
    green=0
    numbersum=0
    text=textbox.get(1.0,2000.0)
    textvalidate=0
    length=len(text)-1
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
                triangle2(int(1*rc), 1)
            if char=="B" or char=="b":
                sine2 (int(1*bc), 1)
            if char=="C" or char=="c":
                sine2(int(2*bc), 2)
            if char=="D" or char=="d":
                sine2(int(3*bc),3)
            if char=="E" or char=="e":
                square2(int(1*gc),1)
            if char=="F" or char=="f":
                square2(int(2*gc),2)
            if char=="G" or char=="g":
                sine2(int(4*bc),4)
            if char=="H" or char=="h":
                square2(int(3*gc),3)
            if char=="i" or char=="I":
                square2(int(4*gc),4)
            if char=="J" or char=="j":
                sine2(int(5*bc),5)
            if char=="K" or char=="k":
                triangle2(int(2*rc),2)
            if char=="L" or char=="l":
                square2(int(5*gc),5)
            if char=="M" or char=="m":
                triangle2(int(3*rc),3)
            if char=="N" or char=="n":
                triangle2(int(4*rc),4)
            if char=="O" or char=="o":
                sine2(int(6*bc),6)
            if char=="P" or char=="p":
                sine2(int(7*bc),7)
            if char=="Q" or char=="q":
                sine2(int(8*bc),8)
            if char=="R" or char=="r":
                sine2(int(9*bc),9)
            if char=="S" or char=="s":
                sine2(int(10*bc),10)
            if char=="T" or char=="t":
                square2(int(5*gc),6)
            if char=="U" or char=="u":
                sine2(int(11*bc),11)
            if char=="V" or char=="v":
                triangle2(int(5*rc),5)
            if char=="W" or char=="w":
                triangle2(int(6*rc),6)
            if char=="X" or char=="x":
                triangle2(int(7*rc),7)
            if char=="Y" or char=="y":
                triangle2(int(8*rc),8)
            if char=="Z" or char=="z":
                triangle2(int(9*rc),9)
    if bluelength>0:
        blue=int(blue/bluelength)
        blue=int(blue*bluelength)
    else:
        blue=0
    if redlength>0:
        red=int(red/redlength)
        red=int(red*redlength)
    else:
        red=0
    if greenlength>0:
        green=int(green/greenlength)
        green=int(green*greenlength)
    else:
        green=0
    RGB=[red,green,blue]
    maxvalue=max(RGB)
    if red>0:
        R=int(255/maxvalue*red)
    else:
        R=0
    if green>0:
        G=int(255/maxvalue*green)
    else:
        G=0
    if blue>0:
        B=int(255/maxvalue*blue)
    else:
        B=0
    maxredlightness=redlength*9
    maxgreenlightness=greenlength*6
    maxbluelightness=bluelength*11
    if maxredlightness>0:
        redlightness=int(100*redsum/maxredlightness)
    else:
        redlightness=0
    if maxgreenlightness>0:
        greenlightness=int(100*greensum/maxgreenlightness)
    else:
        greenlightness=0
    if maxbluelightness>0:
        bluelightness=int(100*bluesum/maxbluelightness)
    else:
        bluelightness=0
    redvalue=int(redlightness*R/100)
    greenvalue=int(greenlightness*G/100)
    bluevalue=int(bluelightness*B/100)
    hexcolor=rgb_hack((redvalue,greenvalue,bluevalue))
    ColorDisplayFrame2.configure(bg=hexcolor)
    RedField2.configure(state='normal')
    RedField2.delete(1.0,2000.0)
    RedField2.insert(INSERT,redvalue)
    RedField2.configure(state='disabled')
    GreenField2.configure(state='normal')
    GreenField2.delete(1.0,2000.0)
    GreenField2.insert(INSERT,greenvalue)
    GreenField2.configure(state='disabled')
    BlueField2.configure(state='normal')
    BlueField2.delete(1.0,2000.0)
    BlueField2.insert(INSERT,bluevalue)
    BlueField2.configure(state='disabled')
    HEXField2.configure(state='normal')
    HEXField2.delete(1.0,2000.0)
    HEXField2.insert(INSERT,hexcolor)
    HEXField2.configure(state='disabled')

#algorithm 3

    blue=0
    red=0
    green=0
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

    if bluelength>0:
        blue=int(blue/bluelength)
        blue=int(blue*bluelength)
    else:
        blue=0
    if redlength>0:
        red=int(red/redlength)
        red=int(red*redlength)
    else:
        red=0
    if greenlength>0:
        green=int(green/greenlength)
        green=int(green*greenlength)
    else:
        green=0
    RGB=[red,green,blue]
    maxvalue=max(RGB)
    R=int(255/maxvalue*red)
    G=int(255/maxvalue*green)
    B=int(255/maxvalue*blue)
    hexcolor=rgb_hack((R,G,B))
    ColorDisplayFrame3.configure(bg=hexcolor)
    RedField3.configure(state='normal')
    RedField3.delete(1.0,2000.0)
    RedField3.insert(INSERT,R)
    RedField3.configure(state='disabled')
    GreenField3.configure(state='normal')
    GreenField3.delete(1.0,2000.0)
    GreenField3.insert(INSERT,G)
    GreenField3.configure(state='disabled')
    BlueField3.configure(state='normal')
    BlueField3.delete(1.0,2000.0)
    BlueField3.insert(INSERT,B)
    BlueField3.configure(state='disabled')
    HEXField3.configure(state='normal')
    HEXField3.delete(1.0,2000.0)
    HEXField3.insert(INSERT,hexcolor)
    HEXField3.configure(state='disabled')
    redsum=0
    greensum=0
    bluesum=0
    redlength=0
    bluelength=0
    greenlength=0

#Generate color hotkey
def GenerateColor_hotkey(event):
    GenerateColor()

#Copy Red
def CopyRedfn(event):
    colorvalue=RedField.get(1.0,1.3)
    pyperclip.copy(colorvalue)

def CopyRedfn2(event):
    colorvalue=RedField2.get(1.0,1.3)
    pyperclip.copy(colorvalue)

def CopyRedfn3(event):
    colorvalue=RedField3.get(1.0,1.3)
    pyperclip.copy(colorvalue)

#Copy Green
def CopyGreenfn(event):
    colorvalue=GreenField.get(1.0,1.3)
    pyperclip.copy(colorvalue)

def CopyGreenfn2(event):
    colorvalue=GreenField2.get(1.0,1.3)
    pyperclip.copy(colorvalue)

def CopyGreenfn3(event):
    colorvalue=GreenField3.get(1.0,1.3)
    pyperclip.copy(colorvalue)

#Copy Blue
def CopyBluefn(event):
    colorvalue=BlueField.get(1.0,1.3)
    pyperclip.copy(colorvalue)

def CopyBluefn2(event):
    colorvalue=BlueField2.get(1.0,1.3)
    pyperclip.copy(colorvalue)

def CopyBluefn3(event):
    colorvalue=BlueField3.get(1.0,1.3)
    pyperclip.copy(colorvalue)

#Copy HEX
def CopyHEXfn():
    colorvalue=HEXField.get(1.0,1.7)
    pyperclip.copy(colorvalue)
    
def CopyHEXfn2():
    colorvalue=HEXField2.get(1.0,1.7)
    pyperclip.copy(colorvalue)

def CopyHEXfn3():
    colorvalue=HEXField3.get(1.0,1.7)
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

#copyHEX_hotkey
def CopyHEXfn_hotkey(event):
        CopyHEXfn ()

def CopyHEXfn2_hotkey(event):
        CopyHEXfn2 ()

def CopyHEXfn3_hotkey(event):
        CopyHEXfn3 ()
        
#main
def main():
    init()
    create_app_window()
    create_textbox()
    create_color_display_frame()
    create_labels_buttons()
    create_menu()

main()
root.mainloop()
