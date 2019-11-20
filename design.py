import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#pagina iniziale
class home(Gtk.Window):
	button=[] #Bottoni presenti nella home
	def __init__(self):
		Gtk.Window.__init__(self,title="Home")
		self.box=Gtk.Box(spacing=6)
		self.add(self.box)
		
		self.bottoni_principali()
        
	def cliccato(self,widget):
		widget.set_property("label","ciao") #cambiamo la proprietà
		widget.get_property("label") #ti da la proprietà di un certo widget
		
	def bottoni_principali(self):
		#nomi dei bottoni
		names_lab=["Conteggio","Statistiche","Impostazioni"]
		for i in range(3):
			#creazione dei tre bottoni principaliù
			self.button.append(Gtk.Button(label=names_lab[i]))
			self.button[i].connect("clicked",self.cliccato)
			self.box.pack_start(self.button[i],True, True , 0)
window = home()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()