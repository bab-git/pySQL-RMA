# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:28:29 2019

@author: Babak Hosseini
"""
import numpy as np
import pandas as pd

#master

def pie_list(table,labels, labels_ID, values, i_rng, ptype):
    
    df_verkauf = price_list.groupby(labels_ID)['umsatznetto'].sum().sort_index(ascending = False)
    df_her1 = table.groupby(labels_ID)[values].sum()    

    for i in df_her1.index:
        df_her1[i]=df_her1[i]/df_verkauf[i]*100
        
#    df_her1[values] = df_her1[values].values/df_verkauf['umsatznetto'].values
    df_her2 = table.groupby(labels_ID)[labels].apply(lambda x: x.iloc[0])
    #df_her3 = pd.DataFrame ({df_her["preis"]})
#    df_her = pd.merge(df_her1,df_her2, on = labels_ID).sort_values(values,ascending=False)
    prices = np.round(df_her1.values,2)
    summ_price = prices.sum().round(2)
    price_ratio = (100*prices/prices.sum()).round(2)
    if labels == labels_ID:
        shorten_names=df_her2.values
    else:
        shorten_names=list(map(lambda x: x[:12]+'.' if len(x)>12 else x,df_her2.values))
    df_her = pd.DataFrame({values:df_her1.values,
                           'Percentage':price_ratio},
                            index = shorten_names).sort_values(by = 'preis',ascending=False)    
#    x = df_her[values].iloc[:i_rng]
#    y = df_her[labels].iloc[:i_rng]
    #df_her.iloc[:i_rng].plot.pie(subplots=True, figsize=(8, 4) , title='hersteller_id')
    
#    fig, ax = plt.subplots()
#    ax.pie(x, labels=y, autopct='%1.1f%%',
#            shadow=True, startangle=90)
    def absolute_value(val,list1,summ):
#        print (summ)
        a = np.round(val*list1.sum()/summ, 2)
#        a = val
        return str(a)+'%'
    
    if ptype == 'pie':
#        df_her[:i_rng].plot.pie(y = 'preis',autopct='%1.1f%%', shadow=True, startangle=90, legend = False)
#        df_her[:i_rng].plot.pie(y = 'preis'
#                                , autopct='%1.1f%%'
#                                , shadow=True, startangle=90, legend = False,
#                                title = 'Price '+ ptype+ ' based on '+labels)
        df_her.iloc[:i_rng].plot.pie(y = 'preis',
                                autopct=lambda x: absolute_value(x,df_her.preis.iloc[:i_rng].values,summ_price)
                                , shadow=True, startangle=90, legend = False
                                , title = 'Price '+ ptype+ ' based on '+labels)
#        df_her[:i_rng].plot.pie(subplots = True, legend = False, title = 'Price '+ ptype+ ' based on '+labels)
#        plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

    elif ptype == 'bar':    
#        df_her[:i_rng].plot.bar(y = 'preis')
        df_her.iloc[:i_rng].plot.bar(subplots = True, title = 'Price '+ ptype+ ' based on '+labels)
#        df_her[:i_rng].plot.bar()
#        df_her[:i_rng].plot.bar(y = 'Percentage', ax = ax)
    return df_her