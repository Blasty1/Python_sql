from SQL import connection   
import datetime
conn=connection('uswJJmW75Q','bxBA2sMC7s','uswJJmW75Q','remotemysql.com')
#conn.write_tables()
conn.inserire_marche()
conn.eliminare_marche()
#conn.inserire_sigarette_vendute()
conn.inserire_stecche_sigarette()
conn.sigarette_vendute()
#conn.registrazione_dati_giornalieri()
conn.drop_today()
