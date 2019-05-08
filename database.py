import SQL  #classe per tutte le funzioni database-programam
import design#classe per la grafica
#connessione al db
conn=SQL.connection('uswJJmW75Q','bxBA2sMC7s','uswJJmW75Q','remotemysql.com')
#creazione finestra principale
window_principale=design.design_home(2,20,65,70,["Conteggio","Storico","Catalogo","Home"],1)
window_principale.aggiunta_spazio(["Cia Mi Chiamo Bruno, Come stai? Io bene anche se la vita fa un po schifo , oh mio dio sto a 86 caratteri mo 100."],45)
#conn.write_tables()
#conn.inserire_marche()
#conn.eliminare_marche()
#conn.sigarette_vendute()
#conn.registrazione_dati_giornalieri()
#conn.drop_today()
#conn.inserire_stecche_sigarette()