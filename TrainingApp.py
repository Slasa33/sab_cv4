from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from tkinter import colorchooser
import MultiListbox as table
from datetime import date
from PIL import Image, ImageTk
from tkinter.font import Font

data = [
       ["Posilování", "2000","Hala", "21.3.2021", "Bartoń", "60 min", "Přinést činky"]]

dataDochazka = [
    ["Posilování", "1.3.2021", "16"], 
    ["Činky", "3.3.2021", "16"], 
    ["Pět na Pět", "5.3.2021", "14"], 
    ["Hala", "7.3.2021", "15"]]

def show_frame(frame):
    frame.tkraise()

class MyProfile():
    def __init__(self, master):
        self.master = master 
        frame3 = Frame(master,width=1366, height=768)
        frame1 = Frame(master, width=1366, height=768)
        frame2 = Frame(master,width=1366, height=768)
        master.resizable(False, False)

        frame1.pack_propagate(0)
        frame2.pack_propagate(0)
        frame3.pack_propagate(0)
        

        for frame in (frame1, frame2, frame3):
            frame.grid(row=0,column=0,sticky='nsew')


        
        #===================================== Frame 1 code =====================================#

        self.leftFrame = Frame(frame1, width=250)
        self.leftFrame.pack(side="left", fill=BOTH)
        self.leftTop = Frame(self.leftFrame)
        self.leftMid = Frame(self.leftFrame)
        self.leftBottom = Frame(self.leftFrame)
        self.leftFrame.pack_propagate(0)

        self.leftTop = LabelFrame(self.leftFrame, text="Účet", font='Helvetica 12 bold')
        self.leftMid = LabelFrame(self.leftFrame, text="Sbírka", font='Helvetica 12 bold')
        self.leftBottom = LabelFrame(self.leftFrame, text="Nástroje", font='Helvetica 12 bold')

        self.leftTop.pack(side="top", padx=5, fill=BOTH, expand=1)
        self.leftMid.pack(fill=BOTH, expand=1, padx=5)
        self.leftBottom.pack(side="bottom", padx=5, fill=BOTH, expand=1)

        boldfontButton = Font(font='Helvetica 12 bold')

        self.profile = Button(self.leftTop, text="Můj profil", padx=10, pady=20, width=18, bg='green', font=boldfontButton,command=lambda:show_frame(frame1))
        #self.profile.pack(fill=X, side="top")
        self.profile.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.trenink = Button(self.leftMid, text="Tréninky", padx=10, pady=20, width=18, font=boldfontButton, command=lambda:show_frame(frame2))
        #self.trenink.pack(fill=X, side="top")
        self.trenink.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        self.dochazka = Button(self.leftMid, text="Docházka", padx=10, pady=20, width=18, font=boldfontButton, command=lambda:show_frame(frame3))
        #self.dochazka.pack(fill=X, side="bottom")
        self.dochazka.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.nastaveni = Button(self.leftBottom, text="Nastavení", font=boldfontButton, padx=10, pady=20, width=18)
        self.nastaveni.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.topFrame = Frame(frame1)
        self.topFrame.pack(side="top", fill=X)
        self.topL = Frame(self.topFrame)
        self.topL.pack(side="left",fill=BOTH)
        self.topR = Frame(self.topFrame)
        self.topR.pack(side="left", fill=BOTH, pady=30)
        self.saveFrame = Frame(self.topFrame)

        self.photo = PhotoImage(file="brutalek.png")
        self.artwork = Label(self.topL, image=self.photo)
        self.artwork.photo = self.photo
        self.artwork.pack(padx=30, pady=30)


        self.nameL = Label(self.topR, text="JMÉNO A PŘÍJMENÍ", font=("Arial", 7), padx=10)
        self.nameL.grid(column = 0, row = 0)
        self.genderL = Label(self.topR, text="POHLAVÍ", font=("Arial", 7), padx=10)
        self.genderL.grid(column = 2, row = 0)
        self.dobL = Label(self.topR, text="DATUM NAROZENÍ", font=("Arial", 7), padx=10)
        self.dobL.grid(column = 4, row = 0)
        self.pinL = Label(self.topR, text="RODNÉ ČÍSLO", font=("Arial", 7), padx=10)
        self.pinL.grid(column = 6, row = 0)

        self.nameI = Label(self.topR, text="Jura Brutalita", font='Helvetica 14 bold', padx=10)
        self.nameI.grid(column = 0, row = 1)
        self.genderI = Label(self.topR, text="Muž", font='Helvetica 14 bold', padx=10)
        self.genderI.grid(column = 2, row = 1)
        self.dobI = Label(self.topR, text="1.1.2000", font='Helvetica 14 bold', padx=10)
        self.dobI.grid(column = 4, row = 1)
        self.pinI = Label(self.topR, text="003132/3321", font='Helvetica 14 bold', padx=10)
        self.pinI.grid(column = 6, row = 1)


        self.stateL = Label(self.topR, text="STÁTNÍ PŘÍSLUŠNOST", font=("Arial", 7))
        self.stateL.grid(column = 0, row = 3, padx=10, pady=(60,0))
        self.citiL = Label(self.topR, text="OBČANSTVÍ", font=("Arial", 7))
        self.citiL.grid(column = 2, row = 3, padx=10, pady=(60,0))
        self.telL = Label(self.topR, text="TELEFON", font=("Arial", 7))
        self.telL.grid(column = 4, row = 3, padx=10, pady=(60,0))
        self.emailL = Label(self.topR, text="EMAIL", font=("Arial", 7))
        self.emailL.grid(column = 6, row = 3, padx=10, pady=(60,0))


        self.stateI = Label(self.topR, text="Česká republika", font='Helvetica 14 bold', padx=10)
        self.stateI.grid(column = 0, row = 4)
        self.citiI = Label(self.topR, text="Občan", font='Helvetica 14 bold', padx=10)
        self.citiI.grid(column = 2, row = 4)
        self.telI = Label(self.topR, text="745874999", font='Helvetica 14 bold', padx=10)
        self.telI.grid(column = 4, row = 4)
        self.emailI = Label(self.topR, text="email@email.cz", font='Helvetica 14 bold', padx=10)
        self.emailI.grid(column = 6, row = 4)

        self.bottomFrame = Frame(frame1)
        self.bottomFrame.pack(fill=BOTH, pady=50)
        self.bottomL = Frame(self.bottomFrame)
        self.bottomL.pack(side="left",fill=BOTH, pady=(0,30))

        self.bottomR = Frame(self.bottomFrame)
        self.bottomR.pack(side="right",fill=BOTH, pady=(0,30))

        self.resicenceL = Label(self.bottomL, text="BYDLIŠTĚ", font='Helvetica 14 bold', padx=10)
        self.resicenceL.grid(column = 0, row = 0)

        self.streetL = Label(self.bottomL, text="ULICE", font=("Arial", 7))
        self.streetL.grid(column = 0, row = 1, padx=10, pady=(10,0))
        self.popisneL = Label(self.bottomL, text="ČÍSLO POPISNÉ", font=("Arial", 7))
        self.popisneL.grid(column = 2, row = 1, padx=10, pady=(10,0))
        self.obecL = Label(self.bottomL, text="OBEC", font=("Arial", 7))
        self.obecL.grid(column = 4, row = 1, padx=10, pady=(10,0))
        self.pscL = Label(self.bottomL, text="PSČ", font=("Arial", 7))
        self.pscL.grid(column = 6, row = 1, padx=10, pady=(10,0))

        self.streetI = Label(self.bottomL, text="Polská", font='Helvetica 14 bold', padx=10)
        self.streetI.grid(column = 0, row = 2)
        self.popisneI = Label(self.bottomL, text="333/32", font='Helvetica 14 bold', padx=10)
        self.popisneI.grid(column = 2, row = 2)
        self.obecI = Label(self.bottomL, text="Karviná-Ráj", font='Helvetica 14 bold', padx=10)
        self.obecI.grid(column = 4, row = 2)
        self.pscI = Label(self.bottomL, text="73401", font='Helvetica 14 bold', padx=10)
        self.pscI.grid(column = 6, row = 2)


        self.klubL = Label(self.bottomR, text="KLUB", font='Helvetica 14 bold', padx=10)
        self.klubL.grid(column = 0, row = 0)

        self.nameclubL = Label(self.bottomR, text="NÁZEV KLUBU", font=("Arial", 7))
        self.nameclubL.grid(column = 0, row = 1, padx=10, pady=(10,0))
        self.teamL = Label(self.bottomR, text="TÝM", font=("Arial", 7))
        self.teamL.grid(column = 2, row = 1, padx=10, pady=(10,0))
        self.activeL = Label(self.bottomR, text="AKTIVNÍ", font=("Arial", 7))
        self.activeL.grid(column = 4, row = 1, padx=10, pady=(10,0))
        self.personalnumberL = Label(self.bottomR, text="OSOBNÍ ČÍSLO", font=("Arial", 7))
        self.personalnumberL.grid(column = 6, row = 1, padx=10, pady=(10,0))

        self.nameclubI = Label(self.bottomR, text="HCB-Karviná", font='Helvetica 14 bold', padx=10)
        self.nameclubI.grid(column = 0, row = 2)
        self.teamI = Label(self.bottomR, text="Mladší žáci", font='Helvetica 14 bold', padx=10)
        self.teamI.grid(column = 2, row = 2)
        self.activeI = Label(self.bottomR, text="Ano", font='Helvetica 14 bold', padx=10)
        self.activeI.grid(column = 4, row = 2)
        self.personalnumberI = Label(self.bottomR, text="JUR032", font='Helvetica 14 bold', padx=10)
        self.personalnumberI.grid(column = 6, row = 2)


        self.nameclubL = Label(self.bottomR, text="HISTORIE TURNAJŮ", font='Helvetica 14 bold')
        self.nameclubL.grid(column = 0, row = 4, padx=10, pady=(10,0))

        self.turnaje = Listbox(self.bottomR, width=50, font='Helvetica 10')
        self.turnaje.insert(0, 'Karviná CUP 2020                                        3. Místo')
        self.turnaje.insert(1, "Považská bystřice CUP                                2. Místo")
        self.turnaje.insert(2, "Prague HANDBALL CUP                              1. Místo")
        self.turnaje.insert(3, "Zlín CUP                                                     1. Místo")
        self.turnaje.insert(4, "Karviná CUP 2019                                        2. Místo")
        self.turnaje.insert(5, "CUP dětské mládeže 2019                            4. Místo")
        self.turnaje.insert(6, "Nitra HANDBALL CUP                                  1. Místo")
        self.turnaje.grid(column = 0, row = 5, pady=(10,0), columnspan=10, padx=(0, 110))



        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self.bottomL, image=render)
        img.image = render
        img.place(x=50, y=220)



        for xx in range(10):
            self.bottomFrame.grid_columnconfigure(xx, minsize=100)

            self.bottomR.grid_rowconfigure(3, minsize=100)
        
        for xx in range(10):
            self.topR.grid_columnconfigure(xx, minsize=100)


        #=====================================Frame 2 code=====================================#


        self.leftFrame = Frame(frame2, width=250)
        self.leftFrame.pack(side="left", fill=BOTH)
        self.leftTop = Frame(self.leftFrame)
        self.leftMid = Frame(self.leftFrame)
        self.leftBottom = Frame(self.leftFrame)
        self.leftFrame.pack_propagate(0)

        self.leftTop = LabelFrame(self.leftFrame, text="Účet", font='Helvetica 12 bold')
        self.leftMid = LabelFrame(self.leftFrame, text="Sbírka", font='Helvetica 12 bold')
        self.leftBottom = LabelFrame(self.leftFrame, text="Nástroje", font='Helvetica 12 bold')

        self.leftTop.pack(side="top", padx=5, fill=BOTH, expand=1)
        self.leftMid.pack(fill=BOTH, expand=1, padx=5)
        self.leftBottom.pack(side="bottom", padx=5, fill=BOTH, expand=1)

        boldfontButton = Font(font='Helvetica 12 bold')

        self.profile = Button(self.leftTop, text="Můj profil", padx=10, pady=20, width=18, font=boldfontButton,command=lambda:show_frame(frame1))
        #self.profile.pack(fill=X, side="top")
        self.profile.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.trenink = Button(self.leftMid, text="Tréninky", padx=10, pady=20, width=18, bg='green', font=boldfontButton, command=lambda:show_frame(frame2))
        #self.trenink.pack(fill=X, side="top")
        self.trenink.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        self.dochazka = Button(self.leftMid, text="Docházka", padx=10, pady=20, width=18, font=boldfontButton, command=lambda:show_frame(frame3))
        #self.dochazka.pack(fill=X, side="bottom")
        self.dochazka.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.nastaveni = Button(self.leftBottom, text="Nastavení", font=boldfontButton, padx=10, pady=20, width=18)
        self.nastaveni.place(relx=0.5, rely=0.5, anchor=CENTER)


        self.topFrame = Frame(frame2)
        self.topFrame.pack(side="top", fill=X)
        self.topL = Frame(self.topFrame)
        self.topL.pack(side="left",fill=X)
        self.topR = Frame(self.topFrame)
        self.topR.pack(side="left")
        self.saveFrame = Frame(self.topFrame)


        self.nb = ttk.Notebook(self.topR)
        self.p1 = Frame(self.nb)
        self.p2 = Frame(self.nb)
        self.nb.add(self.p1, text="Adresa")
        self.nb.add(self.p2, text="Poznámka")
        self.nb.grid(column=2, row=0, padx=25)


        #INFORMACE JMENO-NAZEV

        self.nameL = Label(self.topL, text="Název:", padx=10, pady=3, font=("Arial", 16))
        self.nameL.grid(column = 0, row = 0)
        self.nameT = Text(self.topL, width=15, height=1)
        self.nameT.grid(column=1, row=0)
        self.titleL = Label(self.topL, text="Ročník:", padx=10, pady=3, font=("Arial", 16))
        self.titleL.grid(column = 0, row=1)
        self.titleT = Text(self.topL, width=15, height=1)
        self.titleT.grid(column=1, row=1)


        #INFORMACE ZBYTKOVE

        self.placeL = Label(self.p1, text="Místo:", padx=10, pady=3, font=("Arial", 16))
        self.placeL.grid(column=0, row=0)
        self.placeT = Text(self.p1, width=15, height=1)
        self.placeT.grid(column=1, row=0)
        self.dateL = Label(self.p1, text="Datum:", padx=10, pady=3, font=("Arial", 16))
        self.dateL.grid(column=0, row=1)
        self.dateT = Text(self.p1, width=15, height=1)
        self.dateT.grid(column=1, row=1)
        self.coachL = Label(self.p1, text="Trenér:", padx=10, pady=3, font=("Arial", 16))
        self.coachL.grid(column=0, row=2)
        self.coachT = Text(self.p1, width=15, height=1)
        self.coachT.grid(column=1, row=2)
        self.delkaL = Label(self.p1, text="Délka:", padx=10, pady=3, font=("Arial", 16))
        self.delkaL.grid(column=2, row=0)
        self.delkaT = Text(self.p1, width=5, height=1)
        self.delkaT.grid(column=3, row=0)

        #POZNAMKY

        self.noteL = Label(self.p2, text="Poznámky:", padx=10, pady=3, font=("Arial", 16))
        self.noteL.pack(side = LEFT)
        self.noteT = Text(self.p2, width=25, height=5)
        self.noteT.pack(side = RIGHT, fill = BOTH, expand = True)


        boldFont = Font(size=9,weight = "bold")
        #BUTONY
        self.saveFrame.pack(side="left")
        self.saveFrame.place(relx=.78, rely=.5, anchor="center")
        self.bSave = Button(self.saveFrame, text="Uložit záznam", width=25, height=4, font=boldFont,command = self.edit)
        self.bSave.pack(side = LEFT)
        self.bNew = Button(self.saveFrame, text="Nový záznam", width=25, height=4, font=boldFont, command = self.newZaznam)
        self.bNew.pack(side = LEFT)


        #boldStyle.configure("Bold.TButton", font = ('Sans','10','bold'))
        #boldButton = ttk.Button(formatBar, text = "B", width = 2, style = "Bold.Button")

        #MULTILISTBOX INFO
        self.mlb = table.MultiListbox(frame2, (('Název', 20), ('Ročník', 20), ('Misto', 20), ('Datum', 20), ('Trenér', 20), ('Délka', 20), ('Poznámky', 20)))
        for i in range(len(data)):
            self.mlb.insert(END, (data[i][0], data[i][1],data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        self.mlb.pack(expand=YES,fill=BOTH, padx=10, pady=10)
        self.mlb.subscribe( lambda row: self.trainingDetail( row ) )


        #===================================== Frame 3 code =====================================#

        self.leftFrame = Frame(frame3, width=250)
        self.leftFrame.pack(side="left", fill=BOTH)
        self.leftTop = Frame(self.leftFrame)
        self.leftMid = Frame(self.leftFrame)
        self.leftBottom = Frame(self.leftFrame)
        self.leftFrame.pack_propagate(0)

        self.leftTop = LabelFrame(self.leftFrame, text="Účet", font='Helvetica 12 bold')
        self.leftMid = LabelFrame(self.leftFrame, text="Sbírka", font='Helvetica 12 bold')
        self.leftBottom = LabelFrame(self.leftFrame, text="Nástroje", font='Helvetica 12 bold')

        self.leftTop.pack(side="top", padx=5, fill=BOTH, expand=1)
        self.leftMid.pack(fill=BOTH, expand=1, padx=5)
        self.leftBottom.pack(side="bottom", padx=5, fill=BOTH, expand=1)


        self.bottomFrame3 = Frame(frame3)
        self.bottomFrame3.pack(side="bottom")

        boldfontButton = Font(font='Helvetica 12 bold')

        self.profile = Button(self.leftTop, text="Můj profil", padx=10, pady=20, width=18, font=boldfontButton,command=lambda:show_frame(frame1))
        #self.profile.pack(fill=X, side="top")
        self.profile.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.trenink = Button(self.leftMid, text="Tréninky", padx=10, pady=20, width=18, font=boldfontButton, command=lambda:show_frame(frame2))
        #self.trenink.pack(fill=X, side="top")
        self.trenink.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        self.dochazka = Button(self.leftMid, text="Docházka", padx=10, pady=20, width=18, bg='green', font=boldfontButton, command=lambda:show_frame(frame3))
        #self.dochazka.pack(fill=X, side="bottom")
        self.dochazka.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.nastaveni = Button(self.leftBottom, text="Nastavení", font=boldfontButton, padx=10, pady=20, width=18)
        self.nastaveni.place(relx=0.5, rely=0.5, anchor=CENTER)


        self.topFrameDochazkaTOP = Frame(frame3, relief='raised', bd=2)
        self.topFrameDochazkaTOP.pack(side="top",fill=X,pady=10)
        self.topFrameDochazka = Frame(frame3, relief='raised')
        self.topFrameDochazka.pack(side="top",fill=X)


        #===================================== CISLO, JMENO, PRITOMNOST, POZNAMKY, DATUM =====================================#

        today = date.today()

        self.hrac_cislo = Label(self.topFrameDochazkaTOP, font=('arial',10,'bold'), text='Číslo', padx=2, pady=2, width=15)
        self.hrac_cislo.grid(row=0, column=1, sticky=W)
        self.hrac_jmeno = Label(self.topFrameDochazkaTOP, font=('arial',10,'bold'), text='Jméno', padx=2, pady=2, width=15)
        self.hrac_jmeno.grid(row=0, column=2, sticky=W)
        self.box = Label(self.topFrameDochazkaTOP, font=('arial',10,'bold'), text='Přítomnost', padx=2, pady=2, width=15)
        self.box.grid(row=0, column=4)
        self.hrac_omluva = Label(self.topFrameDochazkaTOP, font=('arial',10,'bold'), text='Omluveno', padx=2, pady=2, width=15)
        self.hrac_omluva.grid(row=0, column=6)
        self.hrac_notes = Label(self.topFrameDochazkaTOP, font=('arial',10,'bold'), text='Poznámky', padx=2, pady=2, width=15)
        self.hrac_notes.grid(row=0, column=8)
        self.datum = Text(self.topFrameDochazkaTOP, padx=2, pady=2, width=15, height=1)
        self.datum.grid(row=0, column=10)
        self.datum.insert('1.0',today)
        self.datum.config(state=DISABLED)
        

        self.hrac1_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='1', padx=2, pady=2, bd=2, width=15)
        self.hrac1_cislo.grid(row=1, column=1, sticky=W)
        self.hrac1_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Jakub Jancicka', padx=2, pady=2, bd=2, width=15)
        self.hrac1_jmeno.grid(row=1, column=2, sticky=W)
        self.box1 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box1['values'] = (' ', 'ANO', 'NE')
        self.box1.current(0)
        self.box1.grid(row=1, column=4)
        self.boxO1 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO1['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO1.current(0)
        self.boxO1.grid(row=1, column=6)
        self.hrac1_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac1_notes.grid(row=1, column=8)


        self.hrac2_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='2', padx=2, pady=2, bd=2, width=15)
        self.hrac2_cislo.grid(row=2, column=1, sticky=W)
        self.hrac2_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Jindřich Korbel', padx=2, pady=2, bd=2, width=15)
        self.hrac2_jmeno.grid(row=2, column=2, sticky=W)
        self.box2 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box2['values'] = (' ', 'ANO', 'NE')
        self.box2.current(0)
        self.box2.grid(row=2, column=4)
        self.boxO2 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO2['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO2.current(0)
        self.boxO2.grid(row=2, column=6)
        self.hrac2_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac2_notes.grid(row=2, column=8)


        self.hrac3_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='3', padx=2, pady=2, bd=2, width=15)
        self.hrac3_cislo.grid(row=3, column=1, sticky=W)
        self.hrac3_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Vladislav Skala', padx=2, pady=2, bd=2, width=15)
        self.hrac3_jmeno.grid(row=3, column=2, sticky=W)
        self.box3 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box3['values'] = (' ', 'ANO', 'NE')
        self.box3.current(0)
        self.box3.grid(row=3, column=4)
        self.boxO3 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO3['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO3.current(0)
        self.boxO3.grid(row=3, column=6)
        self.hrac3_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac3_notes.grid(row=3, column=8)


        self.hrac4_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='4', padx=2, pady=2, bd=2, width=15)
        self.hrac4_cislo.grid(row=4, column=1, sticky=W)
        self.hrac4_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Ludvík Varmuža', padx=2, pady=2, bd=2, width=15)
        self.hrac4_jmeno.grid(row=4, column=2, sticky=W)
        self.box4 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box4['values'] = (' ', 'ANO', 'NE')
        self.box4.current(0)
        self.box4.grid(row=4, column=4)
        self.boxO4 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO4['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO4.current(0)
        self.boxO4.grid(row=4, column=6)
        self.hrac4_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac4_notes.grid(row=4, column=8)

        self.hrac5_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='5', padx=2, pady=2, bd=2, width=15)
        self.hrac5_cislo.grid(row=5, column=1, sticky=W)
        self.hrac5_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Zikmund Matula', padx=2, pady=2, bd=2, width=15)
        self.hrac5_jmeno.grid(row=5, column=2, sticky=W)
        self.box5 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box5['values'] = (' ', 'ANO', 'NE')
        self.box5.current(0)
        self.box5.grid(row=5, column=4)
        self.boxO5 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO5['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO5.current(0)
        self.boxO5.grid(row=5, column=6)
        self.hrac5_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac5_notes.grid(row=5, column=8)

        self.hrac6_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='6', padx=2, pady=2, bd=2, width=15)
        self.hrac6_cislo.grid(row=6, column=1, sticky=W)
        self.hrac6_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Otakar Vytlačil', padx=2, pady=2, bd=2, width=15)
        self.hrac6_jmeno.grid(row=6, column=2, sticky=W)
        self.box6 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box6['values'] = (' ', 'ANO', 'NE')
        self.box6.current(0)
        self.box6.grid(row=6, column=4)
        self.boxO6 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO6['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO6.current(0)
        self.boxO6.grid(row=6, column=6)
        self.hrac6_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac6_notes.grid(row=6, column=8)

        self.hrac7_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='7', padx=2, pady=2, bd=2, width=15)
        self.hrac7_cislo.grid(row=7, column=1, sticky=W)
        self.hrac7_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Řehoř Studnička', padx=2, pady=2, bd=2, width=15)
        self.hrac7_jmeno.grid(row=7, column=2, sticky=W)
        self.box7 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box7['values'] = (' ', 'ANO', 'NE')
        self.box7.current(0)
        self.box7.grid(row=7, column=4)
        self.boxO7 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO7['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO7.current(0)
        self.boxO7.grid(row=7, column=6)
        self.hrac7_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac7_notes.grid(row=7, column=8)

        self.hrac8_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='8', padx=2, pady=2, bd=2, width=15)
        self.hrac8_cislo.grid(row=8, column=1, sticky=W)
        self.hrac8_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='David Hák', padx=2, pady=2, bd=2, width=15)
        self.hrac8_jmeno.grid(row=8, column=2, sticky=W)
        self.box8 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box8['values'] = (' ', 'ANO', 'NE')
        self.box8.current(0)
        self.box8.grid(row=8, column=4)
        self.boxO8 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO8['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO8.current(0)
        self.boxO8.grid(row=8, column=6)
        self.hrac8_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac8_notes.grid(row=8, column=8)

        self.buttonons = Button(self.topFrameDochazka, text="Uložit", width=15, height=4, font=boldFont)
        self.buttonons.grid(row=8, column=10, rowspan=3, padx=(60,0))

        

        self.hrac9_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='9', padx=2, pady=2, bd=2, width=15)
        self.hrac9_cislo.grid(row=9, column=1, sticky=W)
        self.hrac9_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Tibor Kulík', padx=2, pady=2, bd=2, width=15)
        self.hrac9_jmeno.grid(row=9, column=2, sticky=W)
        self.box9 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box9['values'] = (' ', 'ANO', 'NE')
        self.box9.current(0)
        self.box9.grid(row=9, column=4)
        self.boxO9 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO9['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO9.current(0)
        self.boxO9.grid(row=9, column=6)
        self.hrac9_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac9_notes.grid(row=9, column=8)

        self.hrac10_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='10', padx=2, pady=2, bd=2, width=15)
        self.hrac10_cislo.grid(row=10, column=1, sticky=W)
        self.hrac10_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Vlastislav Pop', padx=2, pady=2, bd=2, width=15)
        self.hrac10_jmeno.grid(row=10, column=2, sticky=W)
        self.box10 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box10['values'] = (' ', 'ANO', 'NE')
        self.box10.current(0)
        self.box10.grid(row=10, column=4)
        self.boxO10 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO10['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO10.current(0)
        self.boxO10.grid(row=10, column=6)
        self.hrac10_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac10_notes.grid(row=10, column=8)

        self.hrac11_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='11', padx=2, pady=2, bd=2, width=15)
        self.hrac11_cislo.grid(row=11, column=1, sticky=W)
        self.hrac11_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Svatoslav Med', padx=2, pady=2, bd=2, width=15)
        self.hrac11_jmeno.grid(row=11, column=2, sticky=W)
        self.box11 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box11['values'] = (' ', 'ANO', 'NE')
        self.box11.current(0)
        self.box11.grid(row=11, column=4)
        self.boxO11 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO11['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO11.current(0)
        self.boxO11.grid(row=11, column=6)
        self.hrac11_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac11_notes.grid(row=11, column=8)

        self.hrac12_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='12', padx=2, pady=2, bd=2, width=15)
        self.hrac12_cislo.grid(row=12, column=1, sticky=W)
        self.hrac12_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Mojmír Vaníček', padx=2, pady=2, bd=2, width=15)
        self.hrac12_jmeno.grid(row=12, column=2, sticky=W)
        self.box12 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box12['values'] = (' ', 'ANO', 'NE')
        self.box12.current(0)
        self.box12.grid(row=12, column=4)
        self.boxO12 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO12['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO12.current(0)
        self.boxO12.grid(row=12, column=6)
        self.hrac12_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac12_notes.grid(row=12, column=8)

        self.hrac13_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='13', padx=2, pady=2, bd=2, width=15)
        self.hrac13_cislo.grid(row=13, column=1, sticky=W)
        self.hrac13_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Vladan Reich', padx=2, pady=2, bd=2, width=15)
        self.hrac13_jmeno.grid(row=13, column=2, sticky=W)
        self.box13 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box13['values'] = (' ', 'ANO', 'NE')
        self.box13.current(0)
        self.box13.grid(row=13, column=4)
        self.boxO13 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO13['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO13.current(0)
        self.boxO13.grid(row=13, column=6)
        self.hrac13_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac13_notes.grid(row=13, column=8)

        self.hrac14_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='14', padx=2, pady=2, bd=2, width=15)
        self.hrac14_cislo.grid(row=14, column=1, sticky=W)
        self.hrac14_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Luboš Špičák', padx=2, pady=2, bd=2, width=15)
        self.hrac14_jmeno.grid(row=14, column=2, sticky=W)
        self.box14 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box14['values'] = (' ', 'ANO', 'NE')
        self.box14.current(0)
        self.box14.grid(row=14, column=4)
        self.boxO14 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO14['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO14.current(0)
        self.boxO14.grid(row=14, column=6)
        self.hrac14_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac14_notes.grid(row=14, column=8)

        self.hrac15_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='15', padx=2, pady=2, bd=2, width=15)
        self.hrac15_cislo.grid(row=15, column=1, sticky=W)
        self.hrac15_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Vilém Pompa', padx=2, pady=2, bd=2, width=15)
        self.hrac15_jmeno.grid(row=15, column=2, sticky=W)
        self.box15 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box15['values'] = (' ', 'ANO', 'NE')
        self.box15.current(0)
        self.box15.grid(row=15, column=4)
        self.boxO15 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO15['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO15.current(0)
        self.boxO15.grid(row=15, column=6)
        self.hrac15_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac15_notes.grid(row=15, column=8)

        self.hrac16_cislo = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='16', padx=2, pady=2, bd=2, width=15)
        self.hrac16_cislo.grid(row=16, column=1, sticky=W)
        self.hrac16_jmeno = Label(self.topFrameDochazka, font=('arial',10,'bold'), text='Felix Hrabec', padx=2, pady=2, bd=2, width=15)
        self.hrac16_jmeno.grid(row=16, column=2, sticky=W)
        self.box16 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.box16['values'] = (' ', 'ANO', 'NE')
        self.box16.current(0)
        self.box16.grid(row=16, column=4)
        self.boxO16 = ttk.Combobox(self.topFrameDochazka, state='readonly')
        self.boxO16['values'] = (' ', 'OMLUVENO', 'NEOMLUVENO')
        self.boxO16.current(0)
        self.boxO16.grid(row=16, column=6)
        self.hrac16_notes= Text(self.topFrameDochazka, padx=2, pady=2, bd=2, width=15, height=1)
        self.hrac16_notes.grid(row=16, column=8)


        self.topFrameDochazka.grid_columnconfigure(3, minsize=60)
        self.topFrameDochazka.grid_columnconfigure(5, minsize=85)
        self.topFrameDochazka.grid_columnconfigure(7, minsize=85)

        self.topFrameDochazkaTOP.grid_columnconfigure(3, minsize=60)
        self.topFrameDochazkaTOP.grid_columnconfigure(5, minsize=100)
        self.topFrameDochazkaTOP.grid_columnconfigure(7, minsize=100)
        self.topFrameDochazkaTOP.grid_columnconfigure(9, minsize=60)


        self.mlb2 = table.MultiListbox(self.bottomFrame3, (('Název tréninku', 20), ('Datum', 20), ('Přítomnost hráčů', 20)))
        for i in range(len(dataDochazka)):
            self.mlb2.insert(END, (dataDochazka[i][0], dataDochazka[i][1], dataDochazka[i][2]))
        self.mlb2.pack(expand=YES,fill=BOTH, padx=10, pady=(0, 50))
        self.mlb2.subscribe(self.detail)


    def detail(self, row):
        self.row = row
        self.detail_window()

    def detail_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        DetailWindow(self.newWindow, self.master, self.row)
        self.newWindow.mainloop()

    def trainingDetail(self, row):
        self.row = row
        self.training_window()

    def training_window(self):
        x = messagebox.askquestion("", "Zobrazit detail tréninku?")
        if(x == 'yes'):
            self.master.withdraw()
            self.newWin = Toplevel(self.master)
            DetailTrainingWindow(self.newWin, self.master, self.row)
            self.newWin.mainloop()


    def edit(self):

        zaznam = [self.nameT.get(1.0, END)[:-1], self.titleT.get(1.0, END)[:-1],
                   self.placeT.get(1.0, END)[:-1], self.dateT.get(1.0, END)[:-1], self.coachT.get(1.0, END)[:-1],
                   self.delkaT.get(1.0, END)[:-1], self.noteT.get(1.0, END)[:-1]]

        data.append(zaznam)

        for i in range(len(data)):
            self.mlb.delete(0)
                                                                                                                                                                         
        for i in range(len(data)):
            self.mlb.insert(END, (data[i][0], data[i][1],data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))

    def newZaznam(self):
        self.nameT.delete(1.0, END)
        self.titleT.delete(1.0, END)
        self.placeT.delete(1.0, END)
        self.dateT.delete(1.0, END)
        self.coachT.delete(1.0, END)
        self.delkaT.delete(1.0, END) 
        self.noteT.delete(1.0, END)



class DetailWindow():
    def __init__(self, master, old_window, row):
        self.old_window = old_window
        self.master = master
        self.row = row

        self.topFrame = Frame(master)
        self.topFrame.pack(side="top",fill=X)
        # self.placeL = Label(self.topFrame, text="Místo:", padx=10, pady=3)
        # self.placeL.grid(column=0, row=0)

        self.confirm_button = Button(self.topFrame, text='CONFIRM', bg='green',command = self.confirm_user,width=12,height=3)
        self.confirm_button.pack(pady=40)

    def confirm_user(self):
        self.old_window.deiconify() 
        self.master.withdraw()


class DetailTrainingWindow():
    def __init__(self, master, old_window, row):
        self.old_window = old_window
        self.master = master
        self.row = row
        fram = Frame(self.master, width=1000, height=750)
        self.master.resizable(False, False)
        fram.pack()
        fram.pack_propagate(0)

        self.leftoFrame = Frame(fram)
        self.leftoFrame.pack(side="left", fill=BOTH)

        self.leftoFrameBottom = Frame(self.leftoFrame)
        self.leftoFrameBottom.grid(row=24,column=0)

        self.rightoFrame = Frame(fram)
        self.rightoFrame.pack(side="right",fill=BOTH)

        self.photo = PhotoImage(file="han01.png")
        self.artwork = Label(self.rightoFrame, image=self.photo)
        self.artwork.photo = self.photo
        self.artwork.pack(padx=30, pady=(20,30))

        self.photo = PhotoImage(file="han02.png")
        self.artwork = Label(self.rightoFrame, image=self.photo)
        self.artwork.photo = self.photo
        self.artwork.pack(padx=30, pady=(10,30))


        self.druh = Label(self.leftoFrame, font=('arial',14,'bold'), text='Druh tréninku', fg='blue',padx=2, pady=2, width=15)
        self.druh.grid(row=0, column=0, pady=(10,0))

        self.druh1 = Label(self.leftoFrame, font=('arial',12), text='Herní',padx=2, pady=2, width=15)
        self.druh1.grid(row=2, column=0)

        self.cil = Label(self.leftoFrame, font=('arial',14,'bold'), text='Cíl tréninku', fg='blue',padx=2, pady=2, width=15)
        self.cil.grid(row=4, column=0)

        self.cil1 = Label(self.leftoFrame, font=('arial',12), text='Nácvik útoku',padx=2, pady=2, width=20)
        self.cil1.grid(row=6, column=0)

        self.nacini = Label(self.leftoFrame, font=('arial',14,'bold'), text='Co přinést', fg='blue',padx=2, pady=2, width=15)
        self.nacini.grid(row=8, column=0)

        self.nacini1 = Label(self.leftoFrame, font=('arial',12), text='Balóny, dresy',padx=2, pady=2, width=15)
        self.nacini1.grid(row=10, column=0)


        self.popis = Label(self.leftoFrame, font=('arial',14,'bold'), text='Popis tréninku', fg='blue', pady=2, width=15)
        self.popis.grid(row=12, column=0)

        var = StringVar()
        self.popis1 = Message(self.leftoFrame, font=('arial',12), textvariable=var, width=500)
        self.popis1.grid(row=14, column=0, rowspan=4, columnspan=4, padx=(50,0))

        var.set("Hřiště je rozděleno podle nákresu. Situace je taková, že jsme v útoku. Akce začíná u střeďáka, který zvedne roku. Přihraje pravé spojce a běží dělat clonu pro ní. Spojka uvolní křídlo a to střílí.")

        self.delka = Label(self.leftoFrame, font=('arial',14, 'bold'), text='Délka a trvání', padx=2, fg='blue', pady=2, width=15)
        self.delka.grid(row=20, column=0)

        self.delka1 = Label(self.leftoFrame, font=('arial',12), text='60 minut, střídání útoků co 5 minut',padx=2, pady=2, width=25)
        self.delka1.grid(row=22, column=0)


        self.upravit = Button(self.leftoFrameBottom, text="Upravit", bg='orange',width=15, height=4)
        self.upravit.grid(row=0, column=0, padx=(30,0))

        self.zavrit = Button(self.leftoFrameBottom, text="Zavřít", bg='green',width=15, height=4, command=self.closewind)
        self.zavrit.grid(row=0, column=2)


        #self.leftoFrame.grid_rowconfigure(1, minsize=30)
        self.leftoFrame.grid_rowconfigure(3, minsize=30)
        #self.leftoFrame.grid_rowconfigure(5, minsize=30)
        self.leftoFrame.grid_rowconfigure(7, minsize=30)
        self.leftoFrame.grid_rowconfigure(11, minsize=30)
        self.leftoFrame.grid_rowconfigure(15, minsize=30)
        self.leftoFrame.grid_rowconfigure(19, minsize=30)
        self.leftoFrame.grid_rowconfigure(23, minsize=100)

        self.leftoFrameBottom.grid_columnconfigure(1, minsize=20)

        # self.confirm_button = Button(self.leftoFrame, text='CONFIRM', bg='green',command = self.confirm_user,width=12,height=3)
        # self.confirm_button.pack(pady=40)

    def closewind(self):
        self.old_window.deiconify() 
        self.master.withdraw()



    


root = Tk()
app = MyProfile(root)
root.mainloop()

    

        

        