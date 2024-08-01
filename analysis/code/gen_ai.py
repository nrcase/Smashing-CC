import pandas as pd
import mysql.connector

def lookup(unityID):
    for line in mapping:
        if unityID in line:
            return line.split(',')[1]

df = pd.read_csv('/Users/nrcase/research/cc-repo/cc/statistics/post_study.csv')

df.rename(columns={'For how many tasks, approximately, did you consult the following resources? [Generative AI (e.g. ChatGPT)]': 'Generative AI Usage'}, inplace=True)
relevant = df[['Email Address', 'Generative AI Usage']]

with open('/Users/nrcase/research/cc-repo/cc/processing/mapping.txt', '+r') as file:
    mapping = file.read().splitlines()

for index, row in relevant.iterrows():
    unityID = row['Email Address'].split('@')[0]
    relevant.at[index, 'Email Address'] = lookup(unityID)
    

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)
mycursor = mydb.cursor()
mycursor.execute("USE cc")

for index, row in relevant.iterrows():
    mycursor.execute("UPDATE repos_manual SET gpt = %s WHERE anon = %s", (row['Generative AI Usage'], row['Email Address']))
    mydb.commit()





