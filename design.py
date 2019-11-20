import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class home(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self,title="Home")
        self.button=Gtk.Button(label="cliccami")
        self.button.connect("clicked",self.cliccato)
        self.add(self.button)
        
    def cliccato(self,widget):
        widget.set_property("label","ciao") #cambiamo la proprietà
        widget.get_property("label") #ti da la proprietà di un certo widget
window = home()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()