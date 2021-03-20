from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from tkinter import colorchooser
import MultiListbox as table


data = [
       ["Posilování", "2000","Hala", "21.3.2021", "Bartoń", "60 min", "Přinést činky"]]


def show_frame(frame):
    frame.tkraise()

class MyProfile():
    def __init__(self, master):

        frame2 = Frame(master)
        frame3 = Frame(master)
        frame1 = Frame(master)

        for frame in (frame1, frame2, frame3):
            frame.grid(row=0,column=0,sticky='nsew')

        
        #===================================== Frame 1 code =====================================#

        self.leftFrame = Frame(frame1)
        self.leftFrame.pack(side="left", fill=Y)
        self.leftTop = Frame(self.leftFrame)
        self.leftMid = Frame(self.leftFrame)
        self.leftBottom = Frame(self.leftFrame)

        self.leftTop = LabelFrame(self.leftFrame, text="Účet", font='Helvetica 12 bold')
        self.leftMid = LabelFrame(self.leftFrame, text="Sbírka", font='Helvetica 12 bold')
        self.leftBottom = LabelFrame(self.leftFrame, text="Nástroje", font='Helvetica 12 bold')

        self.leftTop.pack(side="top", padx=5, fill=BOTH, expand=1)
        self.leftMid.pack(fill=BOTH, expand=1, padx=5)
        self.leftBottom.pack(side="bottom", padx=5, fill=BOTH, expand=1)

        self.profile = Button(self.leftTop, text="Můj profil", padx=10, pady=3, command=lambda:show_frame(frame1))
        self.profile.grid(column = 0, row = 0)
        self.trenink = Button(self.leftMid, text="Tréninky", padx=10, pady=3, command=lambda:show_frame(frame2))
        self.trenink.grid(column = 0, row = 0)
        
        self.dochazka = Button(self.leftMid, text="Docházka", padx=10, pady=3, command=lambda:show_frame(frame3))
        self.dochazka.grid(column = 0, row = 1)
        self.trener = Label(self.leftBottom, text="Trenér", padx=10, pady=3)
        self.trener.grid(column = 0, row = 0)

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
        self.dobL = Label(self.topR, text="DATUM NAROYENÍ", font=("Arial", 7), padx=10)
        self.dobL.grid(column = 4, row = 0)
        self.pinL = Label(self.topR, text="RODNÉ ČÍSLO", font=("Arial", 7), padx=10)
        self.pinL.grid(column = 6, row = 0)

        self.nameI = Label(self.topR, text="Jura Brutalita", font='Helvetica 9 bold', padx=10)
        self.nameI.grid(column = 0, row = 1)
        self.genderI = Label(self.topR, text="Muž", font='Helvetica 9 bold', padx=10)
        self.genderI.grid(column = 2, row = 1)
        self.dobI = Label(self.topR, text="1.1.2000", font='Helvetica 9 bold', padx=10)
        self.dobI.grid(column = 4, row = 1)
        self.pinI = Label(self.topR, text="003132/3321", font='Helvetica 9 bold', padx=10)
        self.pinI.grid(column = 6, row = 1)


        self.stateL = Label(self.topR, text="STÁTNÍ PŘÍSLUŠNOST", font=("Arial", 7))
        self.stateL.grid(column = 0, row = 3, padx=10, pady=(60,0))
        self.citiL = Label(self.topR, text="OBČANSTVÍ", font=("Arial", 7))
        self.citiL.grid(column = 2, row = 3, padx=10, pady=(60,0))
        self.telL = Label(self.topR, text="TELEFON", font=("Arial", 7))
        self.telL.grid(column = 4, row = 3, padx=10, pady=(60,0))
        self.emailL = Label(self.topR, text="EMAIL", font=("Arial", 7))
        self.emailL.grid(column = 6, row = 3, padx=10, pady=(60,0))


        self.stateI = Label(self.topR, text="Česká republika", font='Helvetica 9 bold', padx=10)
        self.stateI.grid(column = 0, row = 4)
        self.citiI = Label(self.topR, text="Občan", font='Helvetica 9 bold', padx=10)
        self.citiI.grid(column = 2, row = 4)
        self.telI = Label(self.topR, text="745874999", font='Helvetica 9 bold', padx=10)
        self.telI.grid(column = 4, row = 4)
        self.emailI = Label(self.topR, text="email@email.cz", font='Helvetica 9 bold', padx=10)
        self.emailI.grid(column = 6, row = 4)

        self.bottomFrame = Frame(frame1)
        self.bottomFrame.pack(side="bottom", fill=BOTH)
        self.bottomL = Frame(self.bottomFrame)
        self.bottomL.pack(side="left",fill=BOTH, pady=(0,30))

        self.bottomR = Frame(self.bottomFrame)
        self.bottomR.pack(side="right",fill=BOTH, pady=(0,30))

        self.resicenceL = Label(self.bottomL, text="BYDLIŠTĚ", font='Helvetica 11 bold', padx=10)
        self.resicenceL.grid(column = 0, row = 0)

        self.streetL = Label(self.bottomL, text="ULICE", font=("Arial", 7))
        self.streetL.grid(column = 0, row = 1, padx=10, pady=(10,0))
        self.popisneL = Label(self.bottomL, text="ČÍSLO POPISNÉ", font=("Arial", 7))
        self.popisneL.grid(column = 2, row = 1, padx=10, pady=(10,0))
        self.obecL = Label(self.bottomL, text="OBEC", font=("Arial", 7))
        self.obecL.grid(column = 4, row = 1, padx=10, pady=(10,0))
        self.pscL = Label(self.bottomL, text="PSČ", font=("Arial", 7))
        self.pscL.grid(column = 6, row = 1, padx=10, pady=(10,0))

        self.streetI = Label(self.bottomL, text="Polská", font='Helvetica 9 bold', padx=10)
        self.streetI.grid(column = 0, row = 2)
        self.popisneI = Label(self.bottomL, text="333/32", font='Helvetica 9 bold', padx=10)
        self.popisneI.grid(column = 2, row = 2)
        self.obecI = Label(self.bottomL, text="Karviná-Ráj", font='Helvetica 9 bold', padx=10)
        self.obecI.grid(column = 4, row = 2)
        self.pscI = Label(self.bottomL, text="73401", font='Helvetica 9 bold', padx=10)
        self.pscI.grid(column = 6, row = 2)


        self.klubL = Label(self.bottomR, text="KLUB", font='Helvetica 11 bold', padx=10)
        self.klubL.grid(column = 0, row = 3)

        self.nameclubL = Label(self.bottomR, text="NÁZEV KLUBU", font=("Arial", 7))
        self.nameclubL.grid(column = 0, row = 4, padx=10, pady=(10,0))
        self.teamL = Label(self.bottomR, text="TÝM", font=("Arial", 7))
        self.teamL.grid(column = 2, row = 4, padx=10, pady=(10,0))
        self.activeL = Label(self.bottomR, text="AKTIVNÍ", font=("Arial", 7))
        self.activeL.grid(column = 4, row = 4, padx=10, pady=(10,0))
        self.personalnumberL = Label(self.bottomR, text="OSOBNÍ ČÍSLO", font=("Arial", 7))
        self.personalnumberL.grid(column = 6, row = 4, padx=10, pady=(10,0))

        self.nameclubI = Label(self.bottomR, text="HCB-Karviná", font='Helvetica 9 bold', padx=10)
        self.nameclubI.grid(column = 0, row = 5)
        self.teamI = Label(self.bottomR, text="Mladší žáci", font='Helvetica 9 bold', padx=10)
        self.teamI.grid(column = 2, row = 5)
        self.activeI = Label(self.bottomR, text="Ano", font='Helvetica 9 bold', padx=10)
        self.activeI.grid(column = 4, row = 5)
        self.personalnumberI = Label(self.bottomR, text="JUR032", font='Helvetica 9 bold', padx=10)
        self.personalnumberI.grid(column = 6, row = 5)

        for xx in range(10):
            self.bottomFrame.grid_columnconfigure(xx, minsize=40)
        
        for xx in range(10):
            self.topR.grid_columnconfigure(xx, minsize=40)


        #=====================================Frame 2 code=====================================#


        self.leftFrame = Frame(frame2)
        self.leftFrame.pack(side="left", fill=Y)
        self.leftTop = Frame(self.leftFrame)
        self.leftMid = Frame(self.leftFrame)
        self.leftBottom = Frame(self.leftFrame)

        self.leftTop = LabelFrame(self.leftFrame, text="Účet", font='Helvetica 12 bold')
        self.leftMid = LabelFrame(self.leftFrame, text="Sbírka", font='Helvetica 12 bold')
        self.leftBottom = LabelFrame(self.leftFrame, text="Nástroje", font='Helvetica 12 bold')

        self.leftTop.pack(side="top", padx=5, fill=BOTH, expand=1)
        self.leftMid.pack(fill=BOTH, expand=1, padx=5)
        self.leftBottom.pack(side="bottom", padx=5, fill=BOTH, expand=1)

        self.profile = Button(self.leftTop, text="Můj profil", padx=10, pady=3, command=lambda:show_frame(frame1))
        self.profile.grid(column = 0, row = 0)

        self.trenink = Button(self.leftMid, text="Tréninky", padx=10, pady=3, command=lambda:show_frame(frame2))
        self.trenink .grid(column = 0, row = 0)
        self.dochazka = Button(self.leftMid, text="Docházka", padx=10, pady=3, command=lambda:show_frame(frame3))
        self.dochazka.grid(column = 0, row = 1)

        self.trener = Label(self.leftBottom, text="Trenér", padx=10, pady=3)
        self.trener.grid(column = 0, row = 0)


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

        self.nameL = Label(self.topL, text="Název:", padx=10, pady=3)
        self.nameL.grid(column = 0, row = 0)
        self.nameT = Text(self.topL, width=15, height=1)
        self.nameT.grid(column=1, row=0)
        self.titleL = Label(self.topL, text="Ročník:", padx=10, pady=3)
        self.titleL.grid(column = 0, row=1)
        self.titleT = Text(self.topL, width=15, height=1)
        self.titleT.grid(column=1, row=1)


        #INFORMACE ZBYTKOVE

        self.placeL = Label(self.p1, text="Místo:", padx=10, pady=3)
        self.placeL.grid(column=0, row=0)
        self.placeT = Text(self.p1, width=15, height=1)
        self.placeT.grid(column=1, row=0)
        self.dateL = Label(self.p1, text="Datum:", padx=10, pady=3)
        self.dateL.grid(column=0, row=1)
        self.dateT = Text(self.p1, width=15, height=1)
        self.dateT.grid(column=1, row=1)
        self.coachL = Label(self.p1, text="Trenér:", padx=10, pady=3)
        self.coachL.grid(column=0, row=2)
        self.coachT = Text(self.p1, width=15, height=1)
        self.coachT.grid(column=1, row=2)
        self.delkaL = Label(self.p1, text="Délka:", padx=10, pady=3)
        self.delkaL.grid(column=2, row=0)
        self.delkaT = Text(self.p1, width=5, height=1)
        self.delkaT.grid(column=3, row=0)

        #POZNAMKY

        self.noteL = Label(self.p2, text="Poznámky:", padx=10, pady=3)
        self.noteL.pack(side = LEFT)
        self.noteT = Text(self.p2, width=25, height=5)
        self.noteT.pack(side = RIGHT, fill = BOTH, expand = True)


        #BUTONY
        self.saveFrame.pack(side="left")
        self.saveFrame.place(relx=.78, rely=.5, anchor="center")
        self.bSave = Button(self.saveFrame, text="Uložit záznam", width=15, command = self.edit)
        self.bSave.pack(side = LEFT)
        self.bNew = Button(self.saveFrame, text="Nový záznam", width=15, command = self.newZaznam)
        self.bNew.pack(side = LEFT)

        #MULTILISTBOX INFO
        self.mlb = table.MultiListbox(frame2, (('Název', 20), ('Ročník', 20), ('Misto', 20), ('Datum', 20), ('Trenér', 20), ('Délka', 20), ('Poznámky', 20)))
        for i in range(len(data)):
            self.mlb.insert(END, (data[i][0], data[i][1],data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        self.mlb.pack(expand=YES,fill=BOTH, padx=10, pady=10)
        self.mlb.subscribe( lambda row: self._delete( row ) )


        #===================================== Frame 3 code =====================================#

        self.leftFrame = Frame(frame3)
        self.leftFrame.pack(side="left", fill=Y)
        self.leftTop = Frame(self.leftFrame)
        self.leftMid = Frame(self.leftFrame)
        self.leftBottom = Frame(self.leftFrame)

        self.leftTop = LabelFrame(self.leftFrame, text="Účet", font='Helvetica 12 bold')
        self.leftMid = LabelFrame(self.leftFrame, text="Sbírka", font='Helvetica 12 bold')
        self.leftBottom = LabelFrame(self.leftFrame, text="Nástroje", font='Helvetica 12 bold')

        self.leftTop.pack(side="top", padx=5, fill=BOTH, expand=1)
        self.leftMid.pack(fill=BOTH, expand=1, padx=5)
        self.leftBottom.pack(side="bottom", padx=5, fill=BOTH, expand=1)

        self.profile = Button(self.leftTop, text="Můj profil", padx=10, pady=3, command=lambda:show_frame(frame1))
        self.profile.grid(column = 0, row = 0)

        self.trenink = Button(self.leftMid, text="Tréninky", padx=10, pady=3, command=lambda:show_frame(frame2))
        self.trenink .grid(column = 0, row = 0)
        self.dochazka = Button(self.leftMid, text="Docházka", padx=10, pady=3, command=lambda:show_frame(frame3))
        self.dochazka.grid(column = 0, row = 1)

        self.trener = Label(self.leftBottom, text="Trenér", padx=10, pady=3)
        self.trener.grid(column = 0, row = 0)




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

    
    #Kliknutim na radek v listboxu vyskoci dialog s tim, jestli chceme dany zaznam opravdu vymazat

    def _delete(self, row):
        self.row=row
        x = messagebox.askquestion("", "Vážně chcete odstranit záznam?")
        if(x == 'yes'):
            self.mlb.delete(self.row)
            data.pop(self.row) 



root = Tk()
app = MyProfile(root)
root.mainloop()

    

        

        