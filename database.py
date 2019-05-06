from SQL import connection  #classe per tutte le funzioni database-programam
from design import *#classe per la grafica

conn=connection('uswJJmW75Q','bxBA2sMC7s','uswJJmW75Q','remotemysql.com')
window_principale=design_home(4,30,60,30,["Conteggio","Storico","Catalogo","Home"])

#conn.write_tables()
#conn.inserire_marche()
#conn.eliminare_marche()
#conn.sigarette_vendute()
#conn.registrazione_dati_giornalieri()
#conn.drop_today()
#conn.inserire_stecche_sigarette()