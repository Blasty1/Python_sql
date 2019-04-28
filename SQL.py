import mysql.connector #serve per effettuare operazioni sul db
import datetime #serve per ottenere il datetime corrente
class connection():
    
    #Prendiamo i dati del db per creare una connessione
    def __init__(self,Db_name,Password,User,host):
    #Creiamo una connessione
        try:
            self.conn=mysql.connector.connect(
                host=host,
                user=User,
                passwd=Password,
                database=Db_name
        )
            self.cursor=self.conn.cursor()
        except NameError:
            print(NameError)
            
    #Creiamo tutte le tabelle che ci servono
    def write_tables(self):
        #Creiamo la principale query[0] che conterrà tutte le marche delle sigarette
        #Creiamo la secondaria query[1] che conterrà le vendite giornaliere delle sigarette
        #Creiamo l'ultima per tener conto delle somme totali fatte in un mese
        #query[2] serve per poter aggiungere la foreign keys
        self.query=("CREATE TABLE marche_sig(Id_marche_sig INT PRIMARY KEY,Name VARCHAR(100),Prezzo DECIMAL(3,2))","CREATE TABLE today(Id_today INT AUTO_INCREMENT PRIMARY KEY,Orario_vendita DATETIME DEFAULT NOW(),Id_sigarette INT NOT NULL)","CREATE TABLE sigarette_mensili(Incasso_totale DECIMAL(6,2), Giorno DATETIME PRIMARY KEY,Incasso_personale DECIMAL(5,2))","ALTER TABLE today ADD constraint foreign key(Id_sigarette) REFERENCES marche_sig(Id_marche_sig)")
        for x in self.query:
            self.cursor.execute(x)
            
     #Inseriamo le marche di sigarette possedute nel database
    def inserire_marche(self):
        marca=[]#Le marche che andremo a prendere
        numero_sigarette_da_aggiungere=int(input("Quante sigarette vuoi aggiungere?"))
        for x in range(numero_sigarette_da_aggiungere):
            marca.append([int(input("Spara il codice della sigaretta: ")),input("Nome della sigaretta: "),float(input("Il prezzo della sigaretta: "))])
        querye="INSERT INTO marche_sig(Id_marche_sig,Name,Prezzo) VALUES(%s,%s,%s)"
        self.cursor.executemany(querye,marca)
        self.conn.commit()
    def eliminare_marche(self):
        try: 
            id_sig='' #L'id della sigaretta da eliminare
            id_sig=input("Inserisre l'id della sigaretta da eliminare nel catalogo:  ")
            querye="DELETE FROM marche_sig WHERE Id_marche_sig"+id_sig
            self.cursor.execute(querye)
        except:
            print("Id non trovato, riprova.")
    #nella necessità in cui si vendano stecche di sigarette
    def inserire_stecche_sigarette(self):
        x,y=0,0 #definiamo una variabile che servirà per prendere l'id della sigaretta e l'altra per la quantità di pacchetti venduti
        try:
            while(1):
                y=int(input("Insersci l'id della sigaretta oppure '0' per chiudere: "))
                x=int(input("Inserisci la quantità di pacchetti venduti oppure '0' per chiudere:  "))
                if (y == 0 and x == 0) or y == 0 or x == 0:
                    return 0
                else:
                    querye="INSERT INTO today(Id_sigarette) VALUES(%s)"
                    for z in range(x):
                        self.cursor.execute(querye,(y,))
                        self.conn.commit()
        except:
            print("Sigaretta non presente nel database")
            self.inserire_stecche_sigarette()
                
    
    #Inseriamo le sigarette che stiamo vendendo, una alla volta e creando ogni riga , value è il codice della sigaretta.
    def inserire_sigarette_vendute(self,value):
        try:
            querye="INSERT INTO today(Id_sigarette) VALUES(%s)"
            self.cursor.execute(querye,(value,))
            self.conn.commit()
        except:
            return 0

            
    #Controllare le sigarette vendute giornalmente senza stampare nulla.
    def sigarette_vendute_giornalmente(self):
        #Sigarette serviranno per salvare il nome della sigarette e somma_euro invece per effettuare l'operazioni che ci daranno come risultato il prezzo
        sigarette_ven,somma_euro=[],0
        try:
            #Otteniamo la quantità di sigarette vendute
            querye="SELECT Id_sigarette , COUNT(*) FROM today GROUP BY Id_sigarette"
            self.cursor.execute(querye)
            result=self.cursor.fetchall()
            #otteniamo il prezzo guadagnato e il nome delle sigarette(contenute della tabella principale)
            querye1="SELECT Id_marche_sig,Name,Prezzo FROM marche_sig"
            self.cursor.execute(querye1)
            result2=self.cursor.fetchall()
            for y in result2:
                for x in result:
                    if(x[0] == y[0]):
                        somma_euro=y[2] * x[1] #prezzo per il numero di pacchetti venduti
                        sigarette_ven.append([y[1],somma_euro])  #aggiungiamo alal lista il nome delle sigarette e il guadagno ottenuto
            return sigarette_ven
        except ValueError:
            print(ValueError)
#Stampare le sigarette vendute , richiamando sigarette_vendute_giornalmente
    def sigarette_vendute(self):
        sigarette_ven=self.sigarette_vendute_giornalmente()
        for x in sigarette_ven:
                print("Nome: "+x[0]+"\nIncasso ottenuto: ",x[1])
            
#A fine giornata serve per salvare l'incasso effettuato nel database, utiliziamo la funzione sigarette_vendute_giornalmente
    def registrazione_dati_giornalieri(self):
        try:
            #Prendiamo in analisi l'ultimo giorno in cui c'è stata la registrazione dell'incasso, quindi se il barista tenta di ri-salvare l'incasso di oggi, sarà bloccato.
            querye1="SELECT DAY(Giorno) FROM sigarette_mensili ORDER BY Giorno DESC LIMIT 1"
            self.cursor.execute(querye1)
            result=self.cursor.fetchall()
            if result[0][0] == datetime.datetime.now().day:
                print("Registrazione già pervenuta, mi dispiace.")
            else:
                soldi_total,soldi_personal=0,0#somma dei soldi e soldi incassati dalla tabbacheria 
                sigarette=self.sigarette_vendute_giornalmente() #Otteniamo il nome e i soldi guadagnati nel giorno lavorativo
                #sommiamo i vari pacchetti venduti
                for x in sigarette:
                    soldi_total=soldi_total + x[1]
                soldi_personal=(soldi_total*8)/100
                querye="INSERT INTO sigarette_mensili(Incasso_totale,Giorno,Incasso_personale) VALUES(%s,%s,%s)"
                #salviamo l'importo e anche il datetime
                self.cursor.execute(querye,[soldi_total,datetime.datetime.now(),soldi_personal])
                self.conn.commit()
                print("Oggi hai guadagnato in totale: ",soldi_total,"\nIl tuo incasso effettivo è stato di: ",soldi_personal)
        except ValueError:
            print(ValueError)
            
    #Serve per azzerrare il conteggio delle sigarette vendute giornalmente.
    def drop_today(self):
        #Ci assicuriamo che l'utente non abbia sbagliato a cliccare.
        risposta=input('Sicuro di voler azzerrare la contabilità giornaliera?\nScrivi si per esserne sicuro:  ')
        if risposta == "Si" or risposta == "SI" or risposta =="sI" or risposta == "si":
            querye="DELETE FROM today"
            self.cursor.execute(querye)
            self.conn.commit()
        else:
            print("Annullato.")
    
    

    #Aggiungere record ad una tabella
    def add_rows(self,lista_colonne,dati,tabella):
        colonne,segna_posti='','' #variabili stringhe che formeranno il comando sql
        #Ciclo per ricavare i dati dalle liste delle colonne
        for x in range(len(lista_colonne)):
            segna_posti=segna_posti + '%s'
            colonne=colonne + lista_colonne[x]
            if x != len(lista_colonne)-1:
                colonne=colonne + ', '
                segna_posti=segna_posti + ', '
                
        sql_command="INSERT INTO "+tabella+"("+colonne+") VALUES("+segna_posti+")"
        self.cursor.executemany(sql_command,dati)
        self.conn.commit()
        
        #Controlliamo se i record da aggiungere sono gia presente nel db
    def check_rows(self,tabella,lista_colonna,dati):
        nomi_colonne,the_same_rows='',[]
        #nomi_colonne = variabile temporanea per utilizzare i nomi delle colonne del db
        #the_same_rows= variabile per indicare le rows già presenti nel db
        for x in range(len(lista_colonna)):
            nomi_colonne=nomi_colonne + lista_colonna[x] + ' '
            if x != len(lista_colonna)-1:
                nomi_colonne=nomi_colonne + ','

        #Prendiamo tutte i dati di tutte le colonne della tabella che c'interessano
        sql_command="SELECT "+nomi_colonne+"FROM "+tabella
        self.cursor.execute(sql_command)
        result=self.cursor.fetchall()
        for y in dati:
            if y in result:
                the_same_rows.append(y)
        if not the_same_rows:
            return 0
        else:
            return the_same_rows
        
    
                
            

                
    
            
            