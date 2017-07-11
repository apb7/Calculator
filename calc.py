from Tkinter import *
#from sympy import * #V 1.0 does not uses SymPy yet.
from math import *
root=None
tBox=None
myText=None
st=""

def main():
    global root
    root = Tk()
    root.title("Calculator")
    createTextBox(root)
    frame1=Frame(root)
    
    b1a = Button(frame1, text="0"   , height=1, width=1,
                 command=lambda: buttonPushed("0"))
    b1b = Button(frame1, text=".", height=1, width=1,
                 command=lambda: buttonPushed("."))
    b1c = Button(frame1, text="%", height=1, width=1,
                 command=lambda: buttonPushed("%"))
    b1d = Button(frame1, text="+", height=1, width=1,
                 command=lambda: buttonPushed("+"))
    b1e = Button(frame1, text="=", height=1, width=6,
                 command=lambda: buttonPushed("="))
    b1=[b1a,b1b,b1c,b1d,b1e]
    packButtons(b1)
    
    
    frame2=Frame(root)
    b2a = Button(frame2, text="1", height=1, width=1,
                 command=lambda: buttonPushed("1"))
    b2b = Button(frame2, text="2", height=1, width=1,
                 command=lambda: buttonPushed("2"))
    b2c = Button(frame2, text="3", height=1, width=1,
                 command=lambda: buttonPushed("3"))
    b2d = Button(frame2, text="-", height=1, width=1,
                 command=lambda: buttonPushed("-"))
    b2e = Button(frame2, text="x^y", height=1, width=1,
                 command=lambda: buttonPushed("pow("))
    b2f = Button(frame2, text="sqrt(x)", height=1, width=2,
                 command=lambda: buttonPushed("sqrt("))
    b2 = [b2a, b2b, b2c, b2d, b2e,b2f]
    packButtons(b2)
    
    frame3=Frame(root)
    #addButton(frame3,LEFT,7)
    b3a = Button(frame3, text="4", height=1,width=1,command=lambda: buttonPushed("4"))
    b3b = Button(frame3, text="5", height=1, width=1,
                 command=lambda: buttonPushed("5"))
    b3c = Button(frame3, text="6", height=1, width=1,
                 command=lambda: buttonPushed("6"))
    b3d = Button(frame3, text="*", height=1, width=1,
                 command=lambda: buttonPushed("*"))
    b3e = Button(frame3, text="(", height=1, width=1,
                 command=lambda: buttonPushed("("))
    b3f = Button(frame3, text=")", height=1, width=2,
                 command=lambda: buttonPushed(")"))
    b3 = [b3a, b3b, b3c, b3d, b3e, b3f]
    packButtons(b3)

    frame4=Frame(root)
    b4a = Button(frame4, text="7", height=1, width=1,
                 command=lambda: buttonPushed("7"))
    b4b = Button(frame4, text="8", height=1, width=1,
                 command=lambda: buttonPushed("8"))
    b4c = Button(frame4, text="9", height=1, width=1,
                 command=lambda: buttonPushed("9"))
    b4d = Button(frame4, text="/", height=1, width=1,
                 command=lambda: buttonPushed("/"))
    b4e = Button(frame4, text=",", height=1, width=1,
                 command=lambda: buttonPushed(","))
    b4f = Button(frame4, text="X", height=1, width=2,
                 command=lambda: buttonPushed("X"))
    b4 = [b4a, b4b, b4c, b4d, b4e, b4f]
    packButtons(b4)

    frame1.pack(side=BOTTOM)
    frame2.pack(side=BOTTOM)
    frame3.pack(side=BOTTOM)
    frame4.pack(side=BOTTOM)
    tBox.pack(side=BOTTOM)
    root.mainloop()

def createTextBox(parent):
    global tBox
    global myText
    myText=StringVar()
    myText.set("")
    tBox = Entry(parent,textvariable=myText)
    tBox.focus()
    tBox.bind('<Return>',bind_equals_to)
    

def buttonPushed(i):
    global myText
    global st
    try:
        if i=="=":
            st=tBox.get()
            myText.set(str(eval(st)))
            st=""    
        elif i=="X":
            myText.set("")
            st=""
        else:
            st+=str(i)
            myText.set(st)  

    except ZeroDivisionError:
        myText.set("Division by Zero!")
    except SyntaxError:
        myText.set("Invalid Expression!")
    except ValueError:
        myText.set("Out of Range!")  
    except:
        myText.set("Something went wrong!")          


def packButtons(b):
    for button in b:
        button.pack(side=LEFT)

def bind_equals_to(event):
    buttonPushed("=")
    
if __name__ == '__main__':
    main()
