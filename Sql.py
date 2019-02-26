import mysql.connector
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
            
        
    
                
