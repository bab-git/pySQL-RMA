# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from EGIS_functs import pie_list
import pickle
#from numpy import round
import numpy as np
import pandas as pd
import pypyodbc as db
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf
#from plotly.offline import plot
#import plotly.graph_objs as go
#import plotly.plotly as py


server = 'dwh-dev.zentrale.de'
database = 'STAGING DE'
#username = 'ZENTRALE\Babak Hosseini'
cnxn = db.connect('Driver={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=True')
sys.exit()
#%%============ tables list
QUARY='''
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE 
TABLE_CATALOG = 'STAGING DE'
--xtype = 'U'
AND 
--name = 'ARTIKELUMSATZ'
TABLE_SCHEMA = 'DWData'
'''
table_list = pd.read_sql_query(QUARY,cnxn)
#table_list=table_list['table_name'].sort_values()
#%% ============= search whitin tables
#key='WARENGRUPPE_ID'
key ='WARENGRUPPE_ID'.lower()
#key ='WARENGRUPPE'.lower()
#key='rang'
found_tabels=[]
for table in table_list['table_name']:
    QUARY='''
        SELECT TOP (1) *
        FROM DWData.'''+table
    result = pd.read_sql_query (QUARY,cnxn)
    if key in result.columns:
        found_tabels.append(table)
found_tabels                
#%%==========================  read RMA list 
RMA_QUARY = '''
select 
	--rm.rmaantrag_id
	  rm.artikelnr
	, rm.partner_id
	, rm.VERSENDET_AM 
	, rm.LIEFERANT_ID
	, COUNT (rm.RMAANTRAG_ID) As Menge
	, la.HERSTELLER	
	, bp.preis
	, ar.HERSTELLER_ID	
	, pt.SUCHNAME as PARTNER    
    , ar.BEZEICHNUNG AS artikel
    , ar.ARTIKEL_ID
from [STAGING DE].[DWData].[RMAANTRAG] AS rm
join [STAGING DE].[DWData].bestellung AS b on b.nummer = rm.bestellnr
join [STAGING DE].[DWData].bestellposition AS bp on bp.bestellung_id = b.bestellung_id
join [STAGING DE].[DWData].lieferantenartikel AS la on la.lieferantenartikel_id = bp.lieferantenartikel_id and la.artikelnr = rm.artikelnr
join [STAGING DE].[DWData].ARTIKEL AS ar on ar.ARTIKEL_ID = la.ARTIKEL_ID
join [STAGING DE].DWData.[PARTNER] AS pt on rm.PARTNER_ID = pt.PARTNER_ID

where 
rm.VERSENDET_AM >= '2019.01.01'
and rm.partner_id <> 31982

group by 
	  rm.artikelnr
	, rm.partner_id
	, rm.VERSENDET_AM 
	, bp.preis
	, rm.LIEFERANT_ID
	, la.HERSTELLER	
	, ar.HERSTELLER_ID
    , pt.SUCHNAME
    , ar.BEZEICHNUNG
    , ar.ARTIKEL_ID
ORDER BY HERSTELLER_ID --DESC
'''
RMA_list = pd.read_sql_query (RMA_QUARY,cnxn)
col_list = RMA_list.columns

#-------- fix prices based on menge
RMA_list['preis']=RMA_list['menge'].values*RMA_list['preis'].values
RMA_list=RMA_list.drop(columns = 'menge')

#%% ============================ Purchase list
QUARY = '''
SELECT --TOP (1000) 
      [HERSTELLER_ID]      
      ,[LIEFERANT_ID]      
      ,[PARTNER_ID]      
      ,[ARTIKEL_ID]     
	  ,SUM (UMSATZNETTO) as UMSATZNETTO
 FROM [STAGING DE].[DWData].[ARTIKELUMSATZ]
 WHERE   
     DATUM >= '2019-01-02'
     AND ARTIKEL_ID IS NOT NULL
     AND PARTNER_ID IS NOT NULL
group by
	   [HERSTELLER_ID]      
      ,[LIEFERANT_ID]            
      ,[PARTNER_ID]            
      ,[ARTIKEL_ID]

order by PARTNER_ID
'''
#price_list = pd.read_sql_query (QUARY,cnxn)
#----------------- saving to file
#price_list.to_csv(r'price_list.csv', index = None, header=True) 
price_list = pd.read_csv('price_list.csv')

price_col_list = price_list.columns
#%%==========================  RMA analysis
#fig, ax = plt.subplots()
#df_her = RMA_list.groupby("hersteller_id").preis.sum().sort_values(ascending=False)
#df_her.apply(lambda x: x.iloc[0])
#df_her3 = RMA_list.groupby("hersteller_id")['hersteller'].apply(lambda x: x.iloc[0])
#%% hersteller
i_rng = 10
table = RMA_list
labels_ID = "hersteller_id"
values = 'preis'
labels = 'hersteller'
ptype = 'pie'
#pie_list(table,labels,values,i_rng)    

#%%
labels_ID = "partner_id"
values = 'preis'
labels = 'partner'

#pie_list(table,labels,values,i_rng)

#%%  products
labels_ID = "artikel_id"
values = 'preis'
labels = 'artikel'

#%%  Liferants
labels_ID = "lieferant_id"
values = 'preis'
labels = 'lieferant_id'

#%%  
df_her=pie_list(table,labels,labels_ID,values,i_rng,ptype)

#%% find top costs
ratio=5/5

price=df_her.preis.sort_values(ascending=False).values
summ=0;
i_best = []
for i in range(len(price)):
    if price[:i].sum() > price[i:].sum()*ratio:
        i_best = i
        break
print(i_best)        

#pie_list(table,labels,values,len(table),'bar');
#df_her[i_best-3:i_best+10].plot.bar(subplots = True, ax=ax )
#ax = df_her[:2*i_best].plot.bar(y = 'preis' , color = np.where(df_her.index == df_her.index[i_best],'r','b'))
ax = df_her.iloc[:2*i_best].plot.bar(subplots = True, color = [np.where(df_her.index == df_her.index[i_best],'r','b')])
#df_her.plot.bar(subplots = True, color = [np.where(df_her.index == df_her.index[i_best],'r','b')])
for p in ax[1].patches:
    ax[1].annotate(str(p.get_height().round(2))+'%', (p.get_x()*1.005,p.get_height() * 1.005))

plt.show()
#%%
