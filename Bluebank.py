# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:26:48 2023

@author: anami
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to load json file

json_file= open('loan_data_json.json')
data= json.load(json_file)

#method 2 to load json file
with open('loan_data_json.json')as json_file:
 data=json.load(json_file)


#transform data into dataframe
loandata=pd.DataFrame(data)

#defining unique key
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe data of specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using numpy(np) to get annual income
income=np.exp(loandata['log.annual.inc'])
loandata['Annual income']=income

#working with arrays

#0D array
arr=np.array(12)

#1D array
arr=np.array([1,2,3])

#2D arrays
arr=np.array([[1,2,3],[4,5,6]])



#working with If condition

a=40
b=200

if a<b:
    print('b is greater than a')
    
    
#working with other condition

a=40
b=200
c=1000

if a<b and b<c:
    print('b is greater than a but less than c')
    
    
#working with more condition
a=40
b=200
c=30

if a<b and b<c:
    print('b is greater than a but less than c')
    
    
#working with no met
a=40
b=200
c=30

if b>a and b<c:
    print('b is greater than a but less than c')
    
else:
    print('Condition not met')
    
    
    
#working with if else condition(elif)
a=40
b=200
c=30

if b>a and b<c:
    print('b is greater than a but less than c')
    
elif b>a and b>c:
    print('b is greater than a and c')
    
else:
    print('Condition not met')


#working with or condition
a=40
b=200
c=30

if b>a or b<c:
    print('b is greater than a or less than c')

    
else:
    print('Condition not met')
    
#FICO Score work
fico=790

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

if fico>=300 and fico<400:
    ficocat='Very Poor'
elif fico>=400 and fico<600:
    ficocat='Poor'
elif fico >= 601 and fico < 660:
    ficocat='Fair'
elif fico >= 660 and fico < 780:
    ficocat='Good'
elif fico >=780:
    ficocat='Excellent'
else:
    ficocat='Unknown'
print(ficocat)


#applying for loops to the loan data
length=len(loandata)
ficocat=[]

for x in range(0,length):
    catogary=loandata['fico'][x]
    if catogary>=300 and catogary<400:
        cat='Very Poor'
    elif catogary>=400 and catogary<600:
        cat='Poor'
    elif catogary>= 601 and catogary< 660:
        cat='Fair'
    elif catogary >= 660 and catogary < 700:
        cat='Good'
    elif catogary >=700:
        cat='Excellent'
    else:
        cat='Unknown'
    ficocat.append(cat)
ficocat=pd.Series(ficocat)
loandata['fico category']=ficocat


#while loops
i=1
while i<10:
    print(i)
    i=i+1




 #Using try and except
 
    length=len(loandata)
    ficocat=[]


    for x in range(0,length):
        catogary=loandata['fico'][x]
        try:
            if catogary>=300 and catogary<400:
                cat='Very Poor'
            elif catogary>=400 and catogary<600:
                cat='Poor'
            elif catogary>= 601 and catogary< 660:
                cat='Fair'
            elif catogary >= 660 and catogary < 700:
                cat='Good'
            elif catogary >=700:
                cat='Excellent'
            else:
                cat='Unknown'
        except:
            cat='Error'
         
    ficocat.append(cat)

        
        
#Testing some error
    length=len(loandata)
    ficocat=[]


    for x in range(0,length):
        catogary='red'
         
        try:
            if catogary>=300 and catogary<400:
                cat='Very Poor'
            elif catogary>=400 and catogary<600:
                cat='Poor'
            elif catogary>= 601 and catogary< 660:
                cat='Fair'
            elif catogary >= 660 and catogary < 700:
                cat='Good'
            elif catogary >=700:
                cat='Excellent'
            else:
                cat='Unknown'
        except:
            cat='Error-Unknown'  
            ficocat.append(cat)


#df.loc as conditional case
#df.loc[df[column name]condition, new column name]='value(if the condition is met)'
#for interest rate,new column is wanted;if int rate>0.12 then high else low

loandata.loc[loandata['int.rate']>0.12,'int.rate type']='high'
loandata.loc[loandata['int.rate']<=0.12,'int.rate type']='low'

#number of rows/column by fico catogary
catplot=loandata.groupby(['fico category']).size()
catplot.plot.bar(color='green',width=0.2)
plt.show()

#number of rows/column by purpose
purposecount=loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='red',width=0.2)
plt.show()

#working with scatter plot
ypoint=loandata['Annual income']
xpoint=loandata['dti']
plt.scatter(xpoint,ypoint,color='blue')
plt.show()

#storing in csv
loandata.to_csv('loan_cleaned.csv')





























































































































































































































