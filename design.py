import PySimpleGUI as sg
class Design_home:
    #title_name= nome pagina
    #size_put tuple o lista con size output e input, size_put[0]=size output , size_put[1] = size input
    #name_of_bottoni nomi da dare ai bottoni e le key,una lista composta da varie tuple, ognuna di essa rappresenta un bottone.La tuple è formata dal nome e poi dalla key del bottone.
    def __init__(self,title_name,size_put,name_of_bottoni):
        #colore del background
        self.color_sfondo="#ccffff" #Colore dello sfondo
        self.color_sottosfondo="#e6ffff" #colore dei bottoni e dell'input e output
        self.color_text_general="#80dfff" #colore dei testi in generale
        self.text_font_title=("Times",30) #il font del titolo
        self.text_font_botton=("Courier",15)# il font dei bottoni
    #copiamo nelle variabili della classe tutte le informazioni ricevute [per info leggere i commenti sopra il de __init__]
        self.title_name=title_name
        self.size_put=size_put
        self.name_of_bottoni=name_of_bottoni
        
         #Layout del frame del titolo  edella parte superiore della
        self.layout_frame_top=[
            [sg.Text(self.title_name,size=(60,2),key="_TITLE"+self.title_name+"_",justification="center", background_color=self.color_sfondo,text_color=self.color_text_general,font=self.text_font_title)]
        ]
        #Layout parte destra[output + input]
        self.layout_frame_right=[
            #casella output
            [sg.Output(size=self.size_put[0], background_color=self.color_sottosfondo,text_color=self.color_text_general)],
            #barra formata da input + bottone d'invio
            [sg.InputText("",size=self.size_put[1],background_color=self.color_sottosfondo,text_color=self.color_text_general,key="_INPUT"+title_name+"_"),sg.Button("Invia",size=(5,1),button_color=(self.color_text_general,self.color_sottosfondo),font=("Courier",10))],

            
        ]
        #layout bottoni di uscita o di rimpicciolimento della scheda
        self.layout_frame_bottom=[
            #text serve solamente per far abbassare i due bottoni nel layout, nulla di più.
            [sg.Text("",size=(60,2),background_color=self.color_sfondo)],
            [
            sg.Button("Minimize",button_color=(self.color_text_general,self.color_sfondo),key="_MIN_", auto_size_button=True),
            sg.Button("Close",button_color=(self.color_text_general,self.color_sfondo),key="_CLOSE_",  auto_size_button=True),
            ]
        ]
        ###################################################################Creazione del layout dei Bottoni vari####################################################################################################
        self.layout_frame_left=[]
        #per ogni tuple creiamo un bottone e lo associamo al layout dei bottoni, x[0] indica il nome e x[1] indica la key
        for x in self.name_of_bottoni:
            self.layout_frame_left.append([sg.Button(x[0],size=(20,6),button_color=(self.color_text_general,self.color_sottosfondo),key="_"+x[1]+"_",font=self.text_font_botton)])
        #####################################################################Layout totale della pagina#########################################################################
        self.layout=[
            #Layout frame del titolo
            [sg.Frame("",self.layout_frame_top,border_width=0,pad=(100,0),background_color=self.color_sfondo)],
          #layout dei bottoni
            [sg.Frame("",self.layout_frame_left,key="_FRAME_BOTTONI"+self.title_name+"_",border_width=0,pad=(30,0),background_color=self.color_sfondo,),
             #Layout della casella principale(output+input)
             sg.Frame("",self.layout_frame_right,border_width=0,background_color=self.color_sfondo,)],
             #Bottone invia per inviare nella casella output, si trova affianco a quella output
             [sg.Frame("",self.layout_frame_bottom,border_width=0,background_color=self.color_sfondo,pad=(0,0))]
        ]
        self.window=sg.Window("MANAGER OF CIGARETS",size=(1400,800),location=(0,0),no_titlebar=True,background_color=self.color_sfondo).Layout(self.layout)
