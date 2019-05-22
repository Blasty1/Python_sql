import SQL  #classe per tutte le funzioni database-programam
import design#classe per la grafica
#connessione al db
conn=SQL.connection('uswJJmW75Q','bxBA2sMC7s','uswJJmW75Q','remotemysql.com')
conteggio_singolo=lambda:design.input_output((700,400),((70,500),200))
#variabile con funzione lambda(anonima) per i bottoni
window_conteggio=lambda:design.sotto_finestre(2,20,[20,40],[0,30],["Pacchetto Singolo","Pacchetti multipli","Registrazione Giornaliera"],[conteggio_singolo,""])
window_storico=lambda:design.sotto_finestre(2,20,[20,15],[0,30],["Giornaliero","Mensile","Storico"],["",""])
window_catalogo=lambda:design.sotto_finestre(2,20,[20,15],[0,30],0,0)
#creazione finestra principale
window_principale=design.design_home(2,20,65,70,[0,0],["Conteggio","Storico","Catalogo","Home"],[window_conteggio,window_storico,window_catalogo])


#conn.write_tables()
#conn.inserire_marche()
#conn.eliminare_marche()
#conn.sigarette_vendute()
#conn.registrazione_dati_giornalieri()
#conn.drop_today()
#conn.inserire_stecche_sigarette()