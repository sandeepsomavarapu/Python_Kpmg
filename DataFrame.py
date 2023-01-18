import pandas as pd

df=pd.DataFrame()
print(df)
list=["accenture","kpmg","wipro","dell"]
df1=pd.DataFrame(list)
#print(df1)
dict={'Id':[1,2,3,4,5],'Department':['training','admin','hr','development','management']}
df2=pd.DataFrame(dict)
dict1={'Id':[200,300,400,500],'Department':['hr','loans','banking','development']}
df3=pd.DataFrame(dict1)

#df2.pop('Department')
#print(df2[1:3])
df2=df2.append(df3)
print(df2)
df2=df2.drop(0)
print(df2)
