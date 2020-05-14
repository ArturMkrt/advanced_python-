#1 task
import pandas as pd
data = {'Name':['Jora','Ruzanna','Hayk','Liana','Salbina','Sona','Tatev','Vlad','Nairi'],
         'Surname':['Karyan','Ordyan','Sahakyan','Varosyan','Alaverdyan','Kirakosyan','Alaverdyan','Harutyunyan','Hakobyan'],   
         'sex':['Male','Female','Male','Female','Female','Female','Female','Male','Male'],
         'Age':[28,45,27,25,22,29,20,26,26],
         'Status':['Student','Student','Student','Student','Student','Student','Student','Student','Tutor']
        }
df = pd.DataFrame(data=data,columns=['Name','Surname','sex','Age','Status'])
df= df.set_index('Name')

######################################################
#2 task
import pandas as pd
df = pd.read_csv("netflix_titles.csv") 
df[(df["release_year"] > 2015)&((df["cast"].str.contains("Kevin Spacey"))|(df["cast"].str.contains("Leonardo DiCaprio")))].shape[0]
#######################################################

#3 task 
#version 1
df = df[df["director"].notna()]
dircounts = df.groupby("director").count()["title"]
df['movie'] = df['director'].apply(lambda x: dircounts[x])
#version 2
import pandas as pd
def getTotal(director):
    c = 0
    for x in director:
        c += count[x]
    return c
df  = pd.read_csv('netflix_titles.csv')
df = df[df["director"].notna()]
df['new_director'] = df["director"].str.split(", ")
ex = df[["new_director","title"]].explode("new_director")
count = ex.groupby("new_director").count()["title"]
df["Movie"] = df["new_director"].apply(getTotal)
df.drop('new_director', axis=1)
##########################################

#4 task
import pandas as pd
df = pd.read_csv("netflix_titles.csv")
df = df[df["cast"].notna()]
df['cast'] = df['cast'].str.split(', ')
df = df.explode('cast')
df.reset_index(drop=True, inplace=True)
#################################################
#task 5
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("netflix_titles.csv")
df = df[df['type'].str.contains('Movie')]
df = df[df['date_added'].notna() & df['cast'].notna()]
df = df[df['cast'].str.contains('Antonio Banderas')]
df['date_added'] = pd.to_datetime(df['date_added'])
df.sort_values('date_added',inplace=True)
df['duration']= df['duration'].apply(lambda x:int(x.split(' ')[0]))
plt.figure(figsize=(15,5))
plt.plot(df['date_added'],df['duration'])
plt.ylabel("min")
plt.xlabel("date_added")
plt.xticks(df['date_added'], rotation=90, size=12)
plt.show()
plt.hist(df["duration"],bins=5)
plt.yticks(np.arange(6))
plt.xticks(np.linspace(df ["duration"].min(),df ["duration"].max(),6))
plt.xlabel("min")
plt.ylabel("Count")
plt.show()
#######################################


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def get_month(month):
    return month.split(',')[0].split(' ')[0]
def get_year(year):
    return year.split(',')[1].split(' ')[1]
df = pd.read_csv("netflix_titles.csv")
df = df[df['type'].notna()&df['type'].str.contains('Movie')&df['date_added'].notna()]
df['Sort_by_date'] = df['date_added'].apply(lambda x:get_year(x)+' '+get_month(x))
ex = df.groupby('Sort_by_date').count()['type']
df['Sort_by_date'] = df['Sort_by_date'].apply(lambda x:x + ' -' + str(ex[x]))
df['new_date']=pd.to_datetime(df['date_added'])
df = df.sort_values('new_date')
plt.hist(df["new_date"],bins=30)
plt.show()
df.drop(['new_date'],axis=1,inplace=True)
x = np.array(df['Sort_by_date'].apply(lambda x:x.split('-')[0]))
y = np.array(df['Sort_by_date'].apply(lambda x:int(x.split('-')[1])))
plt.figure(figsize=(15,5))
plt.xticks(rotation=90,size=8)
plt.yticks(np.arange(0,260,10),size=10)
plt.plot(x,y)
plt.show()


################################
import pandas as pd
df = pd.read_csv("netflix_titles.csv")
df['date_added'] = pd.to_datetime(df['date_added'])
df.sort_values('date_added',inplace=True)
df = df[df['date_added'].notna()]
df.reset_index(inplace=True)
df['count'] = 0
x = df.at[0,'date_added']
def get_day(date):
    global x
    b = date - x
    x = date
    return abs(b.days)
df['count'] = df['date_added'].apply(get_day)

#######################################################
import pandas as pd
df = pd.read_csv("netflix_titles.csv")
df = df[df['type'].notna() & df['date_added'].notna() & df['director'].notna()]
df['date_added'] = pd.to_datetime(df['date_added'])
df.sort_values('date_added',inplace=True)
df['director'] = df['director'].str.split(', ')
df = df.explode('director')
df = df.reset_index()
df['new_coloumn'] = df['director'] + '--' + df['date_added'].apply(lambda x:str(x).split(' ')[0])
import time 
x = {}
def get_total(line):
    global x
    director,date = line.split('--')
    date = pd.to_datetime(date)
    if director in x:
        b = date-x[director]
        return abs(b.days)
    else:
        b = -1
        x[director] = date
        return b
df['number of days']= df['new_coloumn'].apply(get_total)

