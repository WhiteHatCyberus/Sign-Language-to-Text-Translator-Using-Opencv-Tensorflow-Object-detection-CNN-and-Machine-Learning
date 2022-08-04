#import module from tkinter for UI
from tkinter import *
import os
import subprocess
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="#DFDFDF")

#root.geometry("300x300")

def function1():
    
    os.system("py create_gestures.py")
    os.system("py flip_images.py")
    os.system("py load_images.py")

def function2():

    os.system("py set_hand_hist.py") #works
    
def function3():

    os.system("py recognize_gesture.py")   

def function4():

    root.destroy()


#stting title for the window
root.title("Sign To Text Converter")

#creating a text label
Label(root, text="Sign->Text Translator",font=("times new roman",20),fg="white",bg="#e51a4c",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="#ffffff",fg='black',command=function1).grid(row=1,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Set Hand Histogram",font=('times new roman',20),bg="#ffffff",fg="#000000",command=function2).grid(row=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button       
Button(root,text="Recognize Gesture as a Character",font=('times new roman',20),bg="#ffffff",fg="black",command=function3).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating fourth button              
Button(root,text="Exit",font=('times new roman',20),bg="#e51a4c",fg="white",command=function4).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
