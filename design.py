import PySimpleGUI as sg
class Design_home:
    def __init__(self):
        #colore del background
        self.color_sfondo="#ccffff" #Colore dello sfondo
        self.color_sottosfondo="#e6ffff" #colore dei bottoni e dell'input e output
        self.color_text_general="#80dfff" #colore dei testi in generale
        self.text_font_title=("Times",30)
        self.text_font_botton=("Courier",15)
        #Layout del frame del titolo
        self.layout_frame=[
            [sg.Text("HOME",size=(60,2),justification="center", background_color=self.color_sfondo,text_color=self.color_text_general,font=self.text_font_title)],
        ]
        #Layout parte destra[output + input]
        self.layout_frame_right=[
            [sg.Output(size=(110,38), background_color=self.color_sottosfondo,text_color=self.color_text_general)],
            [sg.InputText("",size=(110,0),background_color=self.color_sottosfondo,text_color=self.color_text_general,key="_INPUT_"),sg.Button("Invia",size=(5,1),button_color=(self.color_text_general,self.color_sottosfondo),font=("Courier",10))],

            
        ]
        #Bottoni vari
        self.layout_frame_left=[
            [sg.Button("Conteggio",size=(20,6),button_color=(self.color_text_general,self.color_sottosfondo),font=self.text_font_botton)],
            [sg.Button("Catalogo",size=(20,6),button_color=(self.color_text_general,self.color_sottosfondo),font=self.text_font_botton)],
            [sg.Button("Storico",size=(20,6),button_color=(self.color_text_general,self.color_sottosfondo),font=self.text_font_botton)]
        ]
        #Layout totale della pagina
        self.layout=[
            #Layout frame del titolo
            [sg.Frame("",self.layout_frame,border_width=0,pad=(100,0),background_color=self.color_sfondo)],
          #layout dei bottoni
            [sg.Frame("",self.layout_frame_left,border_width=0,pad=(30,0),background_color=self.color_sfondo,),
             #Layout della casella principale(output+input)
             sg.Frame("",self.layout_frame_right,border_width=0,background_color=self.color_sfondo,)],
             #Bottone invia per inviare nella casella output, si trova affianco a quella output
             [sg.Button("Chiudi")],
        ]
        self.window=sg.Window("MANAGER OF CIGARETS",size=(1400,800),location=(0,0),no_titlebar="True",background_color=self.color_sfondo).Layout(self.layout)
