from tkinter import*

class Pretvornik():
    def __init__(self, master):

        naslov = Label(text = "PORABLJENE KALORIJE")
        naslov.grid(row=0, column=1)

        napisDatum = Label(text = "Datum: ")
        napisDatum.grid(row=1, column=0)

        napisTek = Label(text = "TEK: ")
        napisTek.grid(row=3, column=0)

        napisKolo = Label(text = "KOLO: ")
        napisKolo.grid(row=4, column=0)

        napisPlavanje = Label(text = "PLAVANJE: ")
        napisPlavanje.grid(row=5, column=0)



        self.Datum = StringVar(master)
        polje_Datum = Entry(master, textvariable = self.Datum)
        polje_Datum.grid(row=1, column=1)

    

        self.Tek = DoubleVar(master, value=0)
        polje_Tek = Entry(master, textvariable=self.Tek)
        polje_Tek.grid(row=3, column=1)

        EnotaT = Label(text="min")
        EnotaT.grid(row=3, column=2)

        gumb_pretvori_Tek= Label(master, text="Rezultat: ")
        gumb_pretvori_Tek.grid(row=3, column=3)

        self.Tek_Rezultat = DoubleVar(master, value=0)
        polje_Tek_Rezultat = Label(master, textvariable = self.Tek_Rezultat)
        self.Tek.trace("w", self.pretvoriTek)
        polje_Tek_Rezultat.grid(row=3, column=4)

       

        self.Kolo = DoubleVar(master, value=0)
        polje_Kolo = Entry(master, textvariable=self.Kolo)
        self.Kolo.trace("w", self.pretvoriKolo)
        polje_Kolo.grid(row=4, column=1)

        EnotaK = Label(text="min")
        EnotaK.grid(row=4, column=2)

        gumb_pretvori_Kolo= Label(master, text="Rezultat: ")
        gumb_pretvori_Kolo.grid(row=4, column=3)

        self.Kolo_Rezultat = DoubleVar(master, value=0)
        polje_Kolo_Rezultat = Label(master, textvariable = self.Kolo_Rezultat)
        polje_Kolo_Rezultat.grid(row=4, column=4)


        
        self.Plavanje = DoubleVar(master, value=0)
        polje_Plavanje = Entry(master, textvariable=self.Plavanje)
        self.Plavanje.trace("w", self.pretvoriPlavanje)
        polje_Plavanje.grid(row=5, column=1)

        EnotaP = Label(text="min")
        EnotaP.grid(row=5, column=2)

        gumb_pretvori_Plavanje= Label(master, text="Rezultat: ")
        gumb_pretvori_Plavanje.grid(row=5, column=3)

        self.Plavanje_Rezultat = DoubleVar(master, value=0)
        polje_Plavanje_Rezultat = Label(master, textvariable = self.Plavanje_Rezultat)
        polje_Plavanje_Rezultat.grid(row=5, column=4)

             

        Skupaj = Label(text="Skupaj: ")
        Skupaj.grid(row=7, column=3)

        self.Skupna_vsota = DoubleVar(master, value=0)
        polje_Skupna_vsota = Label(master, textvariable = self.Skupna_vsota)
        polje_Skupna_vsota.grid(row=7, column=4)



        gumb_shrani = Button(master, text="SHRANI", command=self.Shrani)
        gumb_shrani.grid(row=8, column=4)

    def posodobi(self):
        self.Skupna_vsota.set(self.Tek_Rezultat.get()+self.Kolo_Rezultat.get()+self.Plavanje_Rezultat.get())
    

    def pretvoriTek(self, *args):
        with open("sport_kalorije.txt") as f:
            sez = []
            for vrstica in f:
                sez += [vrstica.strip().split(',')]
        for i in sez:
            if 'Tek' in i:
                self.Tek_Rezultat.set(int(i[1])*self.Tek.get())
        self.posodobi()
        

    def pretvoriKolo(self, *args):
        with open("sport_kalorije.txt") as f:
            sez = []
            for vrstica in f:
                sez += [vrstica.strip().split(',')]
        for i in sez:
            if 'Kolo' in i:
                self.Kolo_Rezultat.set(int(i[1])*self.Kolo.get())
        self.posodobi()
        

    def pretvoriPlavanje(self, *args):
        with open("sport_kalorije.txt") as f:
            sez = []
            for vrstica in f:
                sez += [vrstica.strip().split(',')]
        for i in sez:
            if 'Plavanje' in i:
                self.Plavanje_Rezultat.set(int(i[1])*self.Plavanje.get())
        self.posodobi()
       




    def Shrani(self):
        with open("dnevnik.txt", "at") as f:
            print("{0} sem pretelovadil {1} kalorij; od tega {2} s tekom, {3} s kolesom in {4} s plavanjem.".format(self.Datum.get(), self.Skupna_vsota.get(), self.Tek_Rezultat.get(), self.Kolo_Rezultat.get(), self.Plavanje_Rezultat.get()), file=f)

    
    



root = Tk()

aplikacija = Pretvornik(root)

root.mainloop()
