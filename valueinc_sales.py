# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:39:09 2023

@author: anami
"""

import pandas as pd
#file.csv=pd.read_csv('file.csv')
data =pd.read_csv('transaction.csv')
data =pd.read_csv('transaction.csv',sep=';')

#sumarry of data
data.info()

#playing around variable
var={'name':'Ana','Adress':'VIC'}

#working with calculations
#defining variable

CostPricePerItem=11.73
SellingPricePerItem=21.11
NumberOfItemPerPurchase=6

#Mathematical Operation Through Tablue

ProfitPerItem=21.11-11.73
ProfitPerItem=SellingPricePerItem-CostPricePerItem

ProfitPerTransaction=NumberOfItemPerPurchase*ProfitPerItem
CostPerTransaction=NumberOfItemPerPurchase*CostPricePerItem
SallingPricePerTransaction=NumberOfItemPerPurchase*SellingPricePerItem

#Cost Per Transaction Column Calculations
#CostPerTransaction=NumberOfItemPerPurchase*CostPricePerItem
#variable=dataframe['Column_name']

CostPerItem=data['CostPerItem']
NumberOfItemsPurchased=data['NumberOfItemsPurchased']
CostPerTransaction=NumberOfItemsPurchased*CostPerItem

#Adding New Column in DataFrame

data['CostPerTransaction']=CostPerTransaction

#Selling Price Per Transaction Column Calculations
#SellingPricePerTransaction=NumberOfItemPerPurchase*SellingPricePerItem
#variable=dataframe['Column_name']

SellingPricePerItem=data['SellingPricePerItem']
NumberOfItemsPurchased=data['NumberOfItemsPurchased']
SalesPerTransaction=SellingPricePerItem*NumberOfItemsPurchased

#Adding New Column in DataFrame

data['SalesPerTransaction']=SalesPerTransaction

#ProfitPerTransaction Column Calculations
#ProfitPerTransaction=SalesPerTransaction-CostPerTransaction

ProfitPerTransaction=SalesPerTransaction-CostPerTransaction
data['ProfitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']

#MarkUp Calculations
#markup=(sellingprice-costprice0/costprice)

data['Markup']=(data['SalesPerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']
data['Markup']=(data['ProfitPerTransaction'])/data['CostPerTransaction']

#rounding markup
roundMarkup=round(data['Markup'],2)
data['Markup']=roundMarkup

#Combining date
#my_date=day+'-'+month+'-'+year

data.info()
print(data['Day'].dtype)

#change column datatype
day=data['Day'].astype(str)
print(day.dtype)
year=data['Year'].astype(str)
print(year.dtype)

my_date=day+'-'+data['Month']+'-'+year
data['Date']=my_date

#using iloc to view specific column and row
data.iloc[0] #view first column data
data.iloc[0:3] #view first three data

data.iloc[-5] #view last 5 data
data.iloc[4,2] #view 4th row,2nd column


#using split function to split ClientKeywords data
#new_var =column.str.split('sep', expand=True)

split_col =data['ClientKeywords'].str.split(',', expand=True)

#adding new column for clientkeywords in data frame

data['Client_Age']=split_col[0]
data['Client_Type']=split_col[1]
data['Contract_Length']=split_col[2]

#Replacing[] from the new columns by using replace function
data['Client_Age']=data['Client_Age'].str.replace('[' ,'')
data['Contract_Length']=data['Contract_Length'].str.replace(']', '')

#Using lower function to change data into lowercase
data['ItemDescription']=data['ItemDescription'].str.lower()

#how to merge files
#bringing new datafiles
seasons=pd.read_csv('value_inc_seasons.csv',sep=';')

#merging new file into data frame
#merging file:   merge_df=pd.merge(old_df,new_frame,on='key')
data=pd.merge(data,seasons,on='Month')

#dropping columns
#df=df.drop('column_name',axis=1)
data=data.drop('ClientKeywords',axis=1)
data=data.drop('Day',axis=1)
data=data.drop('Month',axis=1)
data=data.drop('Year',axis=1)

#export into csv
data.to_csv('Valueinc_sales Cleaned.csv',index=False)


















































