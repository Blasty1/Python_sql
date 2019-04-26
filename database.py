from SQL import connection  #classe per tutte le funzioni database-programam
import PySimpleGUI as sg #classe per la grafica
from design import Design_home#classe per la grafica
conn=connection('uswJJmW75Q','bxBA2sMC7s','uswJJmW75Q','remotemysql.com')
design_home=Design_home()
while(1):
    evento,value=design_home.window.Read()
    if evento == 'Chiudi':
        break
    elif evento == "Conteggio":
        print("L'ESKERE")
    elif evento == "Invia":
        print(value['_INPUT_'])
        design_home.window.FindElement("_INPUT_").Update("")
design_home.window.Close()


#conn.write_tables()
#conn.inserire_marche()
#conn.eliminare_marche()
#conn.inserire_sigarette_vendute()
#conn.inserire_stecche_sigarette()
#conn.sigarette_vendute()
#conn.registrazione_dati_giornalieri()
#conn.drop_today()
