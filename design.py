
from gi.repository import Gtk 
from gi.repository import Gdk

#pagina iniziale
class home(Gtk.Window):
        button=[] #Bottoni presenti nella home
        window_hw=(200,850)
        def __init__(self):
##################################################################################
# va di base e non va modificato, si utilizza il css per modificare con GTK
                screen = Gdk.Screen.get_default()
                provider = Gtk.CssProvider()
                style_context = Gtk.StyleContext()
                style_context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
##################################################################################
                css=b"@import url('home.css');" #importiamo il file home.css
                provider.load_from_data(css) #lo carichiamo
                
                Gtk.Window.__init__(self,title="Home")
                self.set_name("title_home") #creiamo una classe che verrà modificata in css
                self.resize(self.window_hw[1],self.window_hw[0]) #modifichiamo la grandezza della finestra
                self.centrare_finestra() #centriamo la finestra
                self.set_border_width(10) #disrtanza dai bordi della finestra
                self.box=Gtk.Box(spacing=20) #spacing è lo spazio tra i bottoni
                self.add(self.box)
        
                self.bottoni_principali() #creiamo i bottoni
                
        def cliccato(self,widget):
                widget.set_property("label","ciao") #cambiamo la proprietà
                print(self.get_position())

        #Centra la finestra  secondo l'asse x e invece mantiene un po più alto secondo l'asse y
        def centrare_finestra(self):
                window_full=self.get_screen() #otteniamo i valore dello schermo
                new_wh=((window_full.get_width()-self.window_hw[1])/2,(window_full.get_height()-self.window_hw[0])/2-90) #calcolaimo i valori per posizionare la finestra
                self.move(new_wh[0],new_wh[1]) #centriamo la finestra
                
        def bottoni_principali(self):
                #nomi dei bottoni
                names_lab=["Conteggio","Statistiche","Impostazioni"]
                for i in range(3):
                        self.button.append(Gtk.Button(label=names_lab[i]))
                        self.button[i].connect("clicked",self.cliccato)
                        self.box.pack_start(self.button[i],True, True , 0)
                        self.button[i].set_name("label_button_h") #creiamo una classe che verrà modificata in css
window = home()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()