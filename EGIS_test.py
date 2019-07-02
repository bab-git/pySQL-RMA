# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import pandas as pd
import pypyodbc as db
import matplotlib.pyplot as plt
import seaborn as sns

server = 'dwh-dev.zentrale.de'
database = 'STAGING DE'
#username = 'ZENTRALE\Babak Hosseini' 
#password = ''
#cnxn = db.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn = db.connect('Driver={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=True')
sys.exit()
print ('stoped')
#%% 

#cursor.execute('SELECT TOP (10) PARTNERSTATUS_ID, NAME FROM DWData.PARTNERSTATUS')
#db_branch='PARTNERSTATUS'
db_branch='ARTIKELUMSATZ'   #UMSATZ: sales
db_branch='ARTIKEL'   #artike
#db_branch='RMAANTRAG'    #RMA data
#QUARY='SELECT TOP (10) * PARTNERSTATUS_ID, NAME FROM DWData.'+db_branch

#       " ARTIKELNR "\
#       " ,DATUM "\

#QUARY="SELECT COUNT (*) " \

#QUARY="SELECT TOP (1000) * "\
#QUARY="SELECT * "\

#QUARY="SELECT TOP (10) *"\
#QUARY="SELECT COUNT (*) " \
QUARY = "SELECT TOP (1000) * "\
       +" FROM DWData."+db_branch
#       +" WHERE "+"DATUM >= '2019-01-01'"\
#       +" AND ARTIKELNR <> '0'"\
#       +" Order By DATUM desc"
#       +" WHERE "+"versendet_am >= '2019-01-01'"

#       +""
#%% ==========================  array format
while False:       
    cursor = cnxn.cursor()
    cursor.execute(QUARY)
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    
    myresult = cursor.fetchall()
    for x in myresult:
      print(x)
    print('test')  
  
#res = cursor.fetchone() 
#print(res)  
#a="1"\
#wqeqw
#+"2"
#print(a)
  
#PQUARY="SELECT TOP (10) * "\
#        +"FROM DWData.PARTNERSTATUS"  
  
#%%==========================  Pandas format - table with headers
  
SQL_Query = pd.read_sql_query(QUARY,cnxn)
cl_list = SQL_Query.columns
#df = pd.DataFrame(SQL_Query, columns = [cl_list[1],cl_list[0],cl_list[3]])
#df = pd.DataFrame(SQL_Query, columns = ['partner_id,''])
#print(df)

SQL_Query['partner_id'].plot.hist()
data=SQL_Query['partner_id'].value_counts()
SQL_Query['partner_id'].value_counts().sort_index().plot.bar()
SQL_Query['lieferant_id'].value_counts().sort_index().plot.bar()

SQL_Query.groupby('lieferant_id').umsatznetto.sum().plot.bar()


g = sns.FacetGrid(SQL_Query, col='rma_grund', col_wrap=4)
g = g.map(sns.kdeplot,'rmaantrag_id')
g = g.map(sns.distplot,'rmaantrag_id', bins=10, kde=True, color='r')
g = g.map(plt.bar,'rmaantrag_id', bins=10, kde=True, color='r')
