#Importing All Required Modules
'''ALL THESE WORKS ARE DONE BY 

ANKITA SIKDER

STUDENT OF BTECH, IN UEMK

CONTACT NO.: 8583939774

EMAIL ID: ankita.sikder14@gmail.com'''
from CovidUpdates import notifyMe,getData,downdatascsv,downdatasjson
from tkinter import *
from tkinter import messagebox,filedialog
from itertools import count
from PIL import ImageTk,Image

####################################Functionality
###########################################################
#############################################################  Labels
def globalUpdates():
    root = Toplevel()
    root.title('COVID-19 GLOBAL UPDATES')
    root.geometry('1030x300+200+80')
    root.configure(background="black")
    root.iconbitmap('covid19.ico')
    formatlist = []
    path = ''
    IntroLabel = Label(root,text='COVID-19 GLOBAL UPDATES',font=('new roman',21,'italic bold'),bg='red',width=62)
    IntroLabel.place(x=0,y=0)

    EntryLabel = Label(root,text='Notify Country : ',font=('arial',20,'italic bold'),bg='white')
    EntryLabel.place(x=10,y=70)

    FormatLabel = Label(root,text='Download In : ',font=('arial',20,'italic bold'),bg='white')
    FormatLabel.place(x=260,y=150)
    EntryLabel = Label(root,text='Types of Case : ',font=('arial',22,'italic bold'),bg='white')
    EntryLabel.place(x=557,y=70)

    ############################################################# Entry
    ###########################################################--load gif
    class ImageLabel(Label):
        """a label that displays images, and plays them if they are gifs"""
        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            self.loc = 0
            self.frames = []

            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.next_frame()

        def unload(self):
            self.config(image="")
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.loc += 1
                self.loc %= len(self.frames)
                self.config(image=self.frames[self.loc])
                self.after(self.delay, self.next_frame)
    rigthliveCovid= ImageLabel(root)
    rigthliveCovid.pack()
    rigthliveCovid.load('rightcovid.gif')
    rigthliveCovid.place(x=50,y=140)
    leftliveCovid = ImageLabel(root)
    leftliveCovid.pack()
    leftliveCovid.load('leftcovid.gif')
    leftliveCovid.place(x=850,y=140)
    ###########################################################
    #Adding DropDown
    types_of_cases=["Total Deaths",
                    "Total Cases",
                    "New Cases",
                    "New Deaths",
                    "Total Recovered",
                    "All Cases"
                    ]
    countrydata = StringVar()
    ent1 = Entry(root,textvariable=countrydata,font=('arial',20,'italic bold'),relief=RIDGE,bd=2,width=20)
    ent1.insert(0,"in small letters")
    ent1.place(x=220,y=70)
    types_of_cases_data = StringVar()
    types_of_cases_data.set(types_of_cases[5])
    drop=OptionMenu(root,types_of_cases_data,*types_of_cases)
    drop.pack()
    drop.place(x=786,y=70)
    drop.config(font="calibri",width=15)
    def shownoti():
        contryname = countrydata.get()
        types=types_of_cases_data.get()
        if contryname == '':
            contryname = 'world'
        contry,totalcas,newcas,total_death,new_death,total_recover=getData('https://www.worldometers.info/coronavirus/',contryname.lower())
        if contryname.isnumeric() or contryname.isspace() or " " in contryname:
            notifyMe("COVID-19 GLOBAL UPDATES", "GIVE PROPER INPUT..\n INVALID INPUT")
            return
        if(types==types_of_cases[0]):
            notifyMe("COVID-19 GLOBAL UPDATES","IN {}\nTotal Deaths : {}".format(contry,total_death))
            return
        if(types==types_of_cases[1]):
            notifyMe("COVID-19 GLOBAL UPDATES","IN {}\nTotal Cases : {}".format(contry,totalcas))
            return
        if(types==types_of_cases[2]):
            notifyMe("COVID-19 GLOBAL UPDATES","IN {}\nNew Cases : {}".format(contry,newcas))
            return
        if(types==types_of_cases[3]):
            notifyMe("COVID-19 GLOBAL UPDATES","IN {}\nNew Deaths : {}".format(contry,new_death))
            return
        if(types==types_of_cases[4]):
            notifyMe("COVID-19 GLOBAL UPDATES","IN {}\nTotal Recovered : {}".format(contry,total_recover))
            return
        if(types==types_of_cases[5]):
            notifyMe("COVID-19 GLOBAL UPDATES",
                     "IN {}\nTotal Cases : {}\nNew Cases : {}\nTotal Deaths : {}\nNew Deaths : {}\nTotal Recovered : {}".format(
                         contry, totalcas, newcas, total_death, new_death, total_recover))
            return

    def createCSV():
     downdatascsv('https://www.worldometers.info/coronavirus/')
     notifyMe("CREATION SUCCESSFUL","COVID19-UPDATES.csv Saved")
    def createJSON():
     downdatasjson('https://www.worldometers.info/coronavirus/')
     notifyMe("CREATION SUCCESSFUL", "COVID19-UPDATES.json Saved")
    ############################################################  Buttons
    InJson = Button(root,text='.json',bg='yellow',font=('arial',15,'italic bold'),relief=RIDGE,activebackground='green',activeforeground='white',
                    bd=5,width=10,command=createJSON)
    InJson.place(x=470,y=150)
    InCsv = Button(root,text='.csv',bg='yellow',font=('arial',15,'italic bold'),relief=RIDGE,activebackground='green',activeforeground='white',
                    bd=5,width=10,command=createCSV)
    InCsv.place(x=620,y=150)
    ###--------->ADDING DATAS
    Submit = Button(root,text='SHOW NOTIFICATION',bg='red',font=('arial',15,'italic bold'),relief=RIDGE,activebackground='green',activeforeground='white',
                    bd=5,width=30,command=shownoti)
    Submit.place(x=320,y=250)


    #######################---calling Mainloop
    root.mainloop()
