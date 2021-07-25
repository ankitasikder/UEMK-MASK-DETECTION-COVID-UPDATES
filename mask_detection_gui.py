#Import All Required Packages
'''ALL THESE WORKS ARE DONE BY 

ANKITA SIKDER

STUDENT OF BTECH, IN UEMK

CONTACT NO.: 8583939774

EMAIL ID: ankita.sikder14@gmail.com'''
#----------------------------------------->
from plyer import notification
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *
from PIL import Image,ImageTk
from winsound import *
import random
from Detection import livedetect
from CoronaGlobalUpdatessGUI import globalUpdates
poklist=["pok.wav","pok2.wav"]
pokulist=["covidbg1.jpg","covidbg2.jpg","covidbg3.jpg","covidbg.png"]


#------------------------------------------->
#Canvas Window Creation
#-------------------------------------------->
#play clicking tune
clicked = lambda: PlaySound(random.choice(poklist),SND_FILENAME)
#--------------------------------------------->
root = Tk()
root.geometry("675x500+120+120")
root.minsize(675,500)
root.maxsize(675,500)
rootwalpaper=Image.open("covidbg.png")
bgimg=ImageTk.PhotoImage(rootwalpaper)
canvas=Canvas(root,width=675,height=500)
canvas.pack()
canvas.create_image(335,245,image=bgimg)
root.title("FACE MASK DETECTION FOR COVID-19")
pkico=["covidNotificationico.ico","covidNotiIco.ico"]
root.iconbitmap(random.choice(pkico))
#------------------------------------------------->
#Buttons Section
#-------------------------------------------------->
#Button1---->Hand Written Digits Recognition
#Button2---->OCR
#Button3---->Credits
#Button4---->Exit
b1=Button(root,text="LIVE\nDETECTION",font=("BankGothic Md BT",18,"bold"),fg="white",pady=7,padx=5,relief=RAISED,bg="green",activeforeground='white',command=lambda:[clicked(),livedetect()])
#place the b1 button
b1_placing=canvas.create_window(500,130,window=b1)
b2=Button(root,text="GLOBAL\nUPDATES",font=("BankGothic Md BT",18,"bold"),fg="black",padx=20,pady=7,relief=RAISED,bg="green",activeforeground='white',command=lambda:[clicked(),globalUpdates()])
#place the b2 button
b2_placing=canvas.create_window(500,300,window=b2)
b3=Button(root,text=" EXIT ",font=("BankGothic Md BT",25,"bold"),fg="black",padx=31,pady=3,relief=SUNKEN,bg="red",command=lambda:[clicked(),root.quit()])
#place the b4 button
b3_placing=canvas.create_window(120,50,window=b3)
#------------------------------------------------->
#main function
if __name__ == '__main__':
    root.mainloop()
