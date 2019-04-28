from SQL import connection  #classe per tutte le funzioni database-programam
import PySimpleGUI as sg #classe per la grafica
from design import Design_home#classe per la grafica
import mysql.connector #serve per effettuare operazioni sul db
import datetime #serve per ottenere il datetime corrente

conn=connection('uswJJmW75Q','bxBA2sMC7s','uswJJmW75Q','remotemysql.com')
#Grafica home
design_home=Design_home("Home",[(130,35),(125,1)],[("Conteggio","CON"),("Catalogo","CATALOGO"),("Storico","STORICO")])
while(1):
    #impostiamo all'inizio del ciclo che la pagina corrente è la home
    pagina_corrente=design_home.title_name
    #servirà a prendere in input gli evente (cioè ciò che schiaccia l'utente)
    evento,value=design_home.window.Read()
    #se l'utente schiaccia esci allora finirà il ciclo e verrà chiusa la pagina
    if evento == '_CLOSE_':
        break
    elif evento == "_CON_":
        #azioniamo il design della pagina richiesta
        design_conteggio=Design_home("Conteggio",[(130,35),(125,1)],[("Singolo Pacchetto","SINGOLO"),("Pacchetti Multipli","MULTIPLI")])
        #mettiamo non visibile la finestra principale del programma
        design_home.window.Hide()
        storico_eventi=[]
        while(1):
            #nuove variabili che servono per prendere i soliti dati in input
            evento2,value2=design_conteggio.window.Read()
            if evento2 == '_CLOSE_':
                #salviamo la variabile e gli diamo il nome della pagina che abbiamo appena chiusa
                pagina_corrente=design_conteggio.title_name
                design_conteggio.window.Close()
                break
            elif evento2 == "_SINGOLO_":
                #se schiacciamo il bottone singolo, allora scomparirà multiplo 
                design_conteggio.window.FindElement("_MULTIPLI_").Update(visible=False)
                #aggiorniamo lo storico eventi, utile sopratutto quando andremo a richiamare la funzione
                storico_eventi.append(evento2)
                print("INSERISCI ID SIGARETTA: ")
            #Se l'ultimo click dell'utente è stato sul bottone singolo e se l'utente invia qualcosa allora quest'ultimo verrà salvato
            elif storico_eventi[-1] == "_SINGOLO_":
                if conn.inserire_sigarette_vendute(int(value2["_INPUTConteggio_"])) != 0:
                    print("Sigaretta Registrata")
                else:
                    print("Sigaretta non pervenuta nei registri, ritenta.")
                design_conteggio.window.FindElement("_INPUTConteggio_").Update("")
                        
                
    elif evento == "_STORICO_":
        print("Eskere")
    elif evento == "_CATALOGO_":
        print("Catalogo")
    #Se l'ultima pagina parte corrisponde alla home, allora s'ignora questo passaggio, nel caso che abbiamo aperto una pagina prima allora diventa di nuovo visibile la home.
    if pagina_corrente != design_home.title_name:
        design_home.window.UnHide()
        
    design_home.window.FindElement("_INPUTHome_").Update("")
design_home.window.Close()


#conn.write_tables()
#conn.inserire_marche()
#conn.eliminare_marche()
#conn.sigarette_vendute()
#conn.registrazione_dati_giornalieri()
#conn.drop_today()
#conn.inserire_stecche_sigarette()