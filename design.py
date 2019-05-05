import tkinter as tk
class design:
    def __init__(self):
        #Parametri grafica
        self.sfondo="#ff8c69"
        self.color_font="#FFFAFA"
        self.spess_bordi=10
        #Finestra principale
        self.window=tk.Tk()
        self.window.geometry("1360x760") #grandezza schermo
        self.window.title("Sigarette Bryan") #titolo della finestra
        self.window.resizable(False,False) #freeziamo la finestra, cosiche l'utente non puo muoverne le misure
        self.window.configure(bg=self.sfondo)
        
        #Paramenti Bottoni home
        self.h_button_home=7 #height 
        self.w_button_home=40 #width
        self.padx_home=80 #pad dalla tabella ascisse
        self.pady_home=100#pad dalla tabella ordinata
        
        #1 bottone , CONTEGGIO
        self.bottone1=tk.Button(self.window,text="CONTEGGIO",height=self.h_button_home,width=self.w_button_home,bg=self.sfondo,relief="ridge",bd=self.spess_bordi)
        self.bottone1.grid(row=0,column=0,padx=self.padx_home,pady=self.pady_home)
        
        #2 bottone, CATALOGO
        self.bottone2=tk.Button(self.window,text="CATALOGO",height=self.h_button_home,width=self.w_button_home,bg=self.sfondo,relief="groove",bd=self.spess_bordi)
        self.bottone2.grid(row=0,column=1,padx=self.padx_home,pady=self.pady_home)
        
        #3 bottone, STORICO
        self.bottone3=tk.Button(self.window,text="STORICO",height=self.h_button_home,width=self.w_button_home,bg=self.sfondo,relief="ridge",bd=self.spess_bordi)
        self.bottone3.grid(row=0,column=2,padx=self.padx_home,pady=self.pady_home)

        #4 
        
        self.window.mainloop()

de=design()

   