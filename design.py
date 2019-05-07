import tkinter as tk
class design_home:
    #titolo[-1] titolo della pagina 
    #titolo[0] in poi i vari titoli di bottoni 
    def __init__(self,h_button,w_button,padx,pady,titolo):
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
        self.h_button_home=h_button #height 
        self.w_button_home=w_button #width
        self.padx_home=padx #pad dalla tabella ascisse
        self.pady_home=pady#pad dalla tabella ordinata
        self.font=("Times",20)
        
        self.titolo=tk.Label(self.window,text=titolo[-1],fg=self.color_font,font=("Courier",40),bg=self.sfondo)
        self.titolo.grid(row=0,column=1)
        
        #Lista di bottoni vari
        self.bottoni=[]
        #Creiamo i bottoni, inserendoli nella lista che abbiamo precedentemente inizializzato
        for x in range(len(titolo)-1):
            self.bottoni.append(tk.Button(self.window,text=titolo[x],height=self.h_button_home,width=self.w_button_home,bg=self.sfondo,relief="ridge",bd=self.spess_bordi,fg=self.color_font,font=self.font))
            #ancoriamo i singoli bottoni ad una colonna diversa pur rimanendo sulla stessa riga
            self.bottoni[x].grid(row=1,column=x,padx=self.padx_home,pady=self.pady_home)
            
        
        
        self.window.mainloop()


   