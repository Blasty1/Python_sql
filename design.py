from tkinter import *
class home_design:
    def __init__(self,radice):
        self.parents=radice
        self.contenitore1=Frame(radice)
        self.contenitore1.pack()
        
        self.pulsante_conf=Button(self.contenitore1)
        self.pulsante_conf.configure(text="Conferma",background="green",command=self.pulsantepremuto)
        self.pulsante_conf.bind("<Return>",self.pulsantepremuto_a)
        self.pulsante_conf.focus_force() #obblighiamo a mettere il fuoco su questo bottone
        self.pulsante_conf.pack(side=LEFT)
        
        self.pulsante_annull=Button(self.contenitore1)
        self.pulsante_annull.configure(text="Annulla", background="red",command=self.pulsanteannullaprem)
        self.pulsante_annull.bind("<Return>",self.pulsanteannullaprem_a)
        self.pulsante_annull.pack(side=RIGHT)
        
    def pulsantepremuto_a(self,evento):
        self.pulsantepremuto()
    def pulsantepremuto(self):
        if self.pulsante_conf["background"] == 'red':
            self.pulsante_conf["background"] = 'green'
        else:
            self.pulsante_conf["background"] = 'blue'
    def pulsanteannullaprem_a(self,evento):
        self.pulsanteannullaprem()
            
    def pulsanteannullaprem(self):
        self.parents.destroy()
class second_exercise:   
    def __init__(self,radice):
    #COSTANTI UTILI PER IL CONTROLLO DELLA LARGHEZZA ECC...
        larghezza_pulsanti=10
        padx,pad
    
    #FINe  
        self.parents=radice
        self.contenitore1=Frame(radice)
        self.contenitore2=Frame(radice)
        self.contenitore1.pack(side=LEFT)
       # self.contenitore2.pack(side=RIGHT)
        
        self.pulsante1=Button(self.contenitore1)
        self.pulsante1.configure(text="Conferma",background="green",command=self.pulsantepremuto1)
        self.pulsante1.configure(width=larghezza_pulsanti)
        self.pulsante1.pack(side=LEFT)
        
        self.pulsante2=Button(self.contenitore1)
        self.pulsante2.configure(text="Annulla",background="red",command=self.pulsanteannulla,width=larghezza_pulsanti)
        self.pulsante2.pack()
    def pulsantepremuto1(self):
        self.pulsante1["background"]="white"
    def pulsanteannulla(self):
        self.parents.destroy()
        
   

root=Tk()
radice=second_exercise(root)
root.mainloop()
