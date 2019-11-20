#Per aprire su CMD : cd C:\msys64\home\Bryan\Python_sql

import SQL  #classe per tutte le funzioni database-programam
import design#classe per la grafica
#connessione al db
conn=SQL.connection('C8D19YcElg','Uo8XbeON5V','C8D19YcElg','remotemysql.com')
main = home()
main.connect("destroy", Gtk.main_quit)
main.show_all()
Gtk.main()

#conn.write_tables()
#conn.inserire_marche()
#conn.eliminare_marche()
#conn.sigarette_vendute()
#conn.registrazione_dati_giornalieri()
#conn.drop_today()
#conn.inserire_stecche_sigarette()