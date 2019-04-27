from SQL import connection  #classe per tutte le funzioni database-programam
import PySimpleGUI as sg #classe per la grafica
from design import Design_home#classe per la grafica
import mysql.connector #serve per effettuare operazioni sul db
import datetime #serve per ottenere il datetime corrente

conn=connection('uswJJmW75Q','bxBA2sMC7s','uswJJmW75Q','remotemysql.com')

design_home=Design_home("Home",[(130,35),(125,1)],[("Conteggio","CON"),("Catalogo","CATALOGO"),("Storico","STORICO")])
while(1):
    evento,value=design_home.window.Read()
    storico_eventi=[] #teniamo conto degli eventi della gui
    if evento == '_CLOSE_':
        break
    elif evento == "_CON_":    
        design_home.window.Hide()
        while(1):
            design_conteggio=Design_home("Conteggio",[(130,35),(125,1)],[("Pacchetto Singolo","SINGOLO"),("Pacchetti multipli","MULTIPLI")])
            evento,value=design_home.window.Read()
            
        #azioniamo il design della pagina richiesta
    elif evento == "_STORICO_":
        print("Storico")
    elif evento == "_CATALOGO_":
        print("Catalogo")
    elif evento == "_MIN_":
        design_home.window.Minimize()
    design_home.window.FindElement("_INPUTHome_").Update("")
design_home.window.Close()


#conn.write_tables()
#conn.inserire_marche()
#conn.eliminare_marche()
#conn.sigarette_vendute()
#conn.registrazione_dati_giornalieri()
#conn.drop_today()
#conn.inserire_stecche_sigarette()