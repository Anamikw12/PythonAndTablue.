# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:14:16 2023

@author: anami
"""

import pandas as pd
#reading excel file or xlsx file
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
data=pd.read_excel('articles.xlsx')

#summary of data
data.describe()

#summary of column
data.info()

#counting number of articles per source
#format of groupby: df.groupby(['column_to_group'])['column to count'].count()
data.groupby(['source_id'])['article_id'].count()
data.groupby(['source_id'])['engagement_reaction_count'].sum()


#dropping one column
data=data.drop('engagement_comment_plugin_count' , axis=1)

#defining function in python
def thisfunction():
    print('This is my first function')
thisfunction()

#this is a function with variable
# def aboutMe(name, surname, location):
#     print('This is ' + name + ' My surname is '+ surname +' I am from '+ location)
#     return name,surname,location
# a= aboutMe('Anamika','Sinha','Australia')


# #for loop in function
# def favfood(food):
#     for x in food:
#         print('Top food is '+x)
# food=('Sushi','Soup','Fries')
# favfood(food)

#creating a keyword flag
# keyword='crash'
# #creating for loop to isolate each title row
# length=len(data)
# keyword_flag=[]
# for x in range(0,length):
#     heading=data['title'][x]
#     if keyword in heading:
#         flag=1
#     else:
#         flag=0
#     keyword_flag.append(flag)

#creating a function
def keywordflag(keyword):
    length=len(data)
    keyword_flag=[]
    for x in range(0,length):
        try:
            heading=data['title'][x]
            if keyword in heading:
                flag=1
            else:
                flag=0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag=keywordflag('murder')

#adding new column in data dataframe
data['keyword_flag']=pd.Series(keywordflag)

#SentimentIntensityAnalyzer
sent_int=SentimentIntensityAnalyzer()
text=data ['title'][16]
sent=sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding for loop to extract sentiment from each title
title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]

length=len(data)

for x in range(0,length):
    try:
        text=data['title'][x]
        sent_int=SentimentIntensityAnalyzer()
        sent=sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

#converting data into series
title_neg_sentiment= pd.Series(title_neg_sentiment)
title_pos_sentiment= pd.Series(title_pos_sentiment)
title_neu_sentiment= pd.Series(title_neu_sentiment)

#transfering in dataframe
data['title_neg_sentiment']=title_neg_sentiment
data['title_pos_sentiment']=title_pos_sentiment
data['title_neu_sentiment']=title_neu_sentiment

#writing the data into excel sheet
data.to_excel('blogme_cleaned.xlsx',sheet_name='blogmedata',index=False)


































