import tkinter as tk
#design della home con funzioni che serviranno anche alle altre classi
class design_home:
    
    #Serve a far andare a capo il testo non appena incontra i bordi
    #text è il testo da inserire
    #spazio è la variabile che indica i caratteri che massimi da inserire in una label
    def aggiunta_spazio(self,text,spazio):
        #Semplicemente inizializziamo una nuova stringa per poterla restituira a fine funzione
        nuova_stringa=["","",""]
   
        #prendiamo ogni singolo elemento della lista
        for x in range(len(text)):
            #Utilizzato come indice per calcolare quante volte deve essere moltiplicato il numero del testo
            n=1
            #prendiamo ogni singola lettera della parola(compreso spazi)
            #per ogni volta che arriviamo a 45 aumenta n e poi quando vi è un altro caso si moltiplica lo spazio concesso * n , cosiche da non terminare.
            for y in range(len(text[x])):
                if y == spazio*n:
                    nuova_stringa[x]=nuova_stringa[x]+"\n"
                    n=n+1
                nuova_stringa[x]=nuova_stringa[x]+text[x][y]
        return nuova_stringa
                
        
    #text , testo della singola guida        
    def info(self,text):
        #Creazione della guida
        #inizializiamo la lista label home 
        self.label_home=[]
        #creiamo le singole label che ci servono per dare informazioni
        for x in range(len(text)):
            testo_rimpicciolito=self.aggiunta_spazio(text,40)
            self.label_home=tk.Label(text=testo_rimpicciolito[x],width=45,height=20,bg=self.sfondo,font=("Courier",9),fg=self.color_font,bd=6,relief="ridge")
            self.label_home.grid(row=2,column=x)
    
    #Crea una finestra generale e restituisce l'oggetto
    #geometry [0]= lunghezza , geometry [1]= altezza
    def creazione_default(self,geometry):
        #Finestra principale
        window=tk.Tk()
        #recuperiamo e centriamo la finestra 
        larghezza = window.winfo_screenwidth()  #otteniamo la lunghezza dello schermo
        altezza = window.winfo_screenheight()# otteniamo l'altezza massima dello schermo
        x = larghezza//2 - geometry[0]//2
        y = altezza//2 - geometry[1]//2
        window.geometry("%dx%d+%d+%d" % (geometry[0], geometry[1], x, y))
        window.title("Sigarette Bryan") #titolo della finestra
        window.resizable(False,False) #freeziamo la finestra, cosiche l'utente non puo muoverne le misure
        window.configure(bg=self.sfondo)
        return window
        
    #Parametri grafica
    sfondo="#ff8c69"
    color_font="#FFFAFA"
    spess_bordi=10
    font=("Times",20)
    #titolo[-1] titolo della pagina 
    #titolo[0] in poi i vari titoli di bottoni
    #home dovrà avere il valore 1 se ci troviamo nella home principale
    #command è una lista di funzioni che andranno a essere conciliati ai bottoni
    def __init__(self,h_button,w_button,padx,pady,pad_title,titolo,command):
        self.window=self.creazione_default((1360,760)) #creiamo la pagina di default
        #Testo presente per far capire il funzionamento di ogni singolo bottone
        self.guida=[
            "Registrazione delle sigarette vendute giornalmente, con la possibilità di scegliere se inserire le sigarette individualmente(INDIVIDUALE) oppure specificando i pacchetti venduti(MULTIPLI)",
            "Visione delle sigarette vendute, con la possibilità di poter vedere le sigarette vendute giornalmente(OGGI) e le sigarette vendute mensilmente(MESE)",
            "Visione dell'intero catalogo delle sigarette, potendo osservarne i codici e sopratutto i prezzi"
        ]
        
        #Paramenti Bottoni home
        self.h_button_home=h_button #height 
        self.w_button_home=w_button #width
        self.padx_home=padx #pad dalla tabella ascisse
        self.pady_home=pady#pad dalla tabella ordinata
        self.command=command #funzioni che andranno ad essere associate ai vari bottoni
        self.pad_title=pad_title #padx = [0] e pady=[1] per il titolo
        
        self.titolo=tk.Label(self.window,text=titolo[-1],fg=self.color_font,font=("Courier",40),bg=self.sfondo)
        self.titolo.grid(row=0,column=1,padx=self.pad_title[0],pady=self.pad_title[1])
        
        #Lista di bottoni vari
        self.bottoni=[]
        #Creiamo i bottoni, inserendoli nella lista che abbiamo precedentemente inizializzato
        for x in range(len(titolo)-1):
            self.bottoni.append(tk.Button(self.window,text=titolo[x],height=self.h_button_home,width=self.w_button_home,bg=self.sfondo,relief="ridge",bd=self.spess_bordi,fg=self.color_font,font=self.font,command=self.command[x]))
            #Se ci troviamo nella home imponiamo i  bottoni sulla stessa riga[1] se no su righe diverse e sulla stessa colonna.           
            self.bottoni[x].grid(row=1,column=x,padx=self.padx_home,pady=self.pady_home)
        #se la pagina richiamata deve creare la home, allora home sarà uguale a 1 , se no sarà uguale a 0 e verrà ignorata la funzione
            self.info(self.guida)
        self.window.mainloop() #manteniamo aperta la finestra
        
#classe utile per le finestre ramificate 
class sotto_finestre(design_home):    
#h_button height
#w_button width
#pad button è una lista , padx[0] e pady[1]
#pad_title lista padx[0] e pady[1]
#command è una lista composta da funzioni che devono attivarsi quando schiacciamo un pulsante       
    def __init__(self,h_button,w_button,pad_button,pad_title,titolo,command):
        #parametri bottoni
        self.h_button=h_button
        self.w_button=w_button
        self.pad_button=pad_button
        self.pad_title=pad_title
        self.command=command
    
        self.window=self.creazione_default((1360,760)) #creiamo la finestra
        #titolo
        self.titolo=tk.Label(self.window,text=titolo[-1],fg=self.color_font,font=("Courier",40),bg=self.sfondo)
        self.titolo.pack(padx=self.pad_title[0],pady=self.pad_title[1])
        
        #finestra dei bottoni
        self.bottoni=[]
        #creazione dei bottoni tutti di lato a sinistra
        for x in range(len(titolo)-1):              
            self.bottoni.append(tk.Button(self.window,text=titolo[x],height=self.h_button,width=self.w_button,bg=self.sfondo,relief="ridge",bd=self.spess_bordi,fg=self.color_font,font=self.font,command=self.command[x]))
            self.bottoni[x].pack(padx=self.pad_button[0],pady=self.pad_button[1])
        
            
        self.window.mainloop()#mantieni la finestra aperta
            
#classe riguardante l'input dei dati e l'output, con tanto di finestra temporanea     
class input_output(design_home):
     #serve per mostrare in oupt ciò che viene scritto nell'input
    #field_inp.delete serve a eliminare il testo che abbiamo scritto nell'input dopo averlo inviato
    def input_output_testo(self,field_inp,field_out):
        self.testo=field_inp.get()
        field_out.config(text=self.testo)
        field_inp.delete(0,12222)
    #una lista composta da [0] = x e [1]= y aventi le dimensioni per creare la finestra
    #inp_outp lista di dimensioni utili alla costruzioni di label di output e di barre di input
    #inp_outp[0] dimensione input/output width, primo numero input secondo output
    #input_outp[1] dimensione output height
    def __init__(self,dimensioni,inp_outp):
        self.dimen=dimensioni
        self.io=inp_outp
        self.window=self.creazione_default(self.dimen)#creazione finestra
        #Centrare cella
        self.centr=self.dimen[0]-self.io[0][0]*7
        
        #FRAME OUTPUT
        #creiamo il frame contenente l'ouput che è formato da varie label
        self.frame_output=tk.Frame(self.window,height=self.io[1],width=int(self.io[0][1]),bd=5,bg=self.sfondo,relief="ridge")
        self.frame_output.grid(row=0,column=0,padx=int(self.centr/2),pady=10)
        
        #Creiamo riga output
        self.output_text=tk.Label(self.frame_output,text="Bau",bd=0,height=7,width=32,bg=self.sfondo)
        self.output_text.grid(row=0,column=0)
      
        
        #Creazione

        
        #FRAME INPUT
        #Creiamo il frame e regoliamo il pad della colonna di conseguenza
        self.frame_o= tk.Frame(self.window, bg=self.sfondo)
        self.frame_o.grid(row=1,column=0)
    
        #creazione riga input
        self.entry_text=tk.Entry(self.frame_o,width=self.io[0][0])
        self.entry_text.grid(row=1,column=0)#/2 per centrarlo
        self.command=lambda:self.input_output_testo(self.entry_text,self.output_text)
        #creazione bottone invia
        #self.io[0][0] è la lunghezza dell'input , che diviso due ci darà la lunghezza del bottone.
        self.button1=tk.Button(self.frame_o,text="Invio",width=self.io[0][0]//2,bg=self.sfondo,relief="ridge",bd=3,fg=self.color_font,font=("Helvete",8),command=self.command)
        self.button1.grid(row=2,column=0,pady=10)
        
        self.window.mainloop()
        
        
            
        
        
 


   