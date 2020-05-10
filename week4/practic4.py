import pandas as pd
group = {'Name':['Jora','Ruzanna','Hayk','Liana','Salbina','Sona','Tatev','Vlad','Nairi'],
         'Surname':['Karyan','Ordyan','Sahakyan','Varosyan','Alaverdyan','Kirakosyan','Alaverdyan','Harutyunyan','Hakobyan'],   
         'sex':['Male','Female','Male','Female','Female','Female','Female','Male','Male'],
         'Age':[28,45,27,25,22,29,20,26,26],
         'Status':['Student','Student','Student','Student','Student','Student','Student','Student','Tutor']
        }
df = pd.DataFrame(group,columns=['Name','Surname','sex','Age','Status'])
df=  df.set_index('Name')
print(df)